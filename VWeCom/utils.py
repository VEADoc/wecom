import base64
import json
from enum import EnumMeta
import random
import time
from typing import Union
from Crypto.Cipher import AES
import io, base64, binascii, hashlib, string, struct,re
from random import choice

class WeComCrypto(object):
    """加解密模块 网上找的
    https://www.sxfblog.com/index.php/archives/388.html"""
    def __init__(self, encodingAesKey, key):
        self.encodingAesKey = encodingAesKey
        self.key = key
        self.aesKey = base64.b64decode(self.encodingAesKey + '=')

    def encrypt(self, content):
        """
        加密
        """
        msg_len = self.length(content)
        content = self.generateRandomKey(16) + msg_len.decode() + content + self.key
        contentEncode = self.pks7encode(content)
        iv = self.aesKey[:16]
        aesEncode = AES.new(self.aesKey, AES.MODE_CBC, iv)
        aesEncrypt = aesEncode.encrypt(contentEncode)
        return base64.b64encode(aesEncrypt).decode().replace('\n', '')

    def length(self, content):
        """
        将msg_len转为符合要求的四位字节长度
        """
        l = len(content)
        return struct.pack('>l', l)

    def pks7encode(self, content):
        """
        安装 PKCS#7 标准填充字符串
        """
        l = len(content)
        output = io.StringIO()
        val = 32 - (l % 32)
        for _ in range(val):
            output.write('%02x' % val)
        return bytes(content, 'utf-8') + binascii.unhexlify(output.getvalue())

    def pks7decode(self, content):
        nl = len(content)
        val = int(binascii.hexlify(content[-1].encode()), 16)
        if val > 32:
            raise ValueError('Input is not padded or padding is corrupt')
        l = nl - val
        return content[:l]

    def decrypt(self, content):
        """
        解密数据
        """
        # 钉钉返回的消息体
        content = base64.b64decode(content)
        iv = self.aesKey[:16]  # 初始向量
        aesDecode = AES.new(self.aesKey, AES.MODE_CBC, iv)
        decodeRes = aesDecode.decrypt(content)[20:].decode().replace(self.key, '')
        # 获取去除初始向量，四位msg长度以及尾部corpid
        return self.pks7decode(decodeRes)

    def generateRandomKey(self, size,
                          chars=string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits):
        """
        生成加密所需要的随机字符串
        """
        return ''.join(choice(chars) for i in range(size))

    def generateSignature(self, nonce, timestamp, token, msg_encrypt):
        """
        生成签名
        """
        signList = ''.join(sorted([nonce, timestamp, token, msg_encrypt])).encode()
        return hashlib.sha1(signList).hexdigest()


class MultiFillClass(object):
    """多重嵌套解析类"""
    
    def __init__(self, params: Union[dict, str] = {}):
        self.__params: dict = params if isinstance(
            params, dict) else json.loads(params)
        self._set_self()

    def _set_self(self):
        for k, v in self.__params.items():
            inner_key = f'_{k}'
            if hasattr(self, inner_key):
                param_class = getattr(self, inner_key).__class__
                if issubclass(param_class, MultiFillClass):
                    new_afc = object.__new__(param_class)
                    new_afc.__init__(v)
                    setattr(self, inner_key, new_afc)
                    continue
                if type(param_class) == EnumMeta:
                    if type(v) == int:
                        setattr(self, inner_key, param_class[[ i for i in param_class.__members__.keys() ][v]])
                        continue
                    
                    """忽略大小写"""
                    match_key = [ k for k in param_class.__members__.keys() if re.match(v,k,re.I) ]
                    if match_key:
                        setattr(self, inner_key, param_class[match_key[0]])
                        continue

                    un_known = [ k for k in param_class.__members__.keys() if re.match(r'^un_?known$',k,re.I) ]
                    if not un_known:
                        continue
                    setattr(self, inner_key, param_class[un_known[0]])

                    continue
                setattr(self, inner_key, v)

    def __str__(self):
        return json.dumps(self.__params,indent=4)

    def __repr__(self):
        return self.__str__()

    def is_empty(self):
        return self.__params == {}

    def not_empty(self):
        return not self.is_empty()

    def to_dict(self):
        """原始信息"""
        return self.__params
    
    def to_json(self):
        """原始信息转为json"""
        return json.dumps(self.__params,ensure_ascii=True)


def wework_jsapi_sign(jsapi_ticket, url):
    """企业微信 JSAPI 签名"""
    
    resp = {
        'noncestr': ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15)),
        'jsapi_ticket': jsapi_ticket,
        'timestamp': int(time.time()),
        'url': url
    }
    sign_string = '&'.join(['%s=%s' % (key.lower(), resp[key]) for key in sorted(resp)])
    sha = hashlib.sha1(sign_string.encode('utf-8'))
    encrypts = sha.hexdigest()
    resp['signature'] = encrypts
    return resp

def _get_md5(raw):
    '''获取md5'''
    m2 = hashlib.md5()
    m2.update(raw.encode(encoding='utf-8'))
    return m2.hexdigest()