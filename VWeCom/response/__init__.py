from typing import List
from ..utils import MultiFillClass


class WeComResponseBase(MultiFillClass):
    """企业微信返回类 基类"""

    def __init__(self, params = {}):
        self._errcode : int = None
        self._errmsg : str = ''
        super().__init__(params=params)
    
    @property
    def errcode(self):
        '''返回码'''
        return self._errcode

    @property
    def errmsg(self):
        '''对返回码的文本描述内容'''
        return self._errmsg
    
class WeComGetAccessTokenRes(WeComResponseBase):
    """### 获取access_token 返回类
    文档地址 : https://work.weixin.qq.com/api/doc/90000/90135/91039
    """

    def __init__(self, params = {}):
        self._access_token : str = ''
        self._expires_in : int = None
        super().__init__(params=params)

    @property
    def access_token(self):
        '''access_token'''
        return self._access_token
    
    @property
    def expires_in(self):
        '''过期时间'''
        return self._expires_in
    
class WeComJSApiTicketRes(WeComResponseBase):
    """获取jsapi票据 返回类"""

    def __init__(self, params = {}):
        self._expires_in : int = None
        self._ticket : str = ''
        super().__init__(params=params)
    
    @property
    def expires_in(self):
        '''过期时间'''
        return self._expires_in

    @property
    def ticket(self):
        '''票据'''
        return self._ticket
    
class WeComGetUserInfoRes(WeComResponseBase):
    """### 获取访问用户身份 返回类
    文档地址 : https://work.weixin.qq.com/api/doc/90000/90135/91023
    """

    def __init__(self, params = {}):
        self._UserId : str = ''
        self._OpenId : str = ''
        self._DeviceId : str = ''
        super().__init__(params=params)
    
    @property
    def user_id(self):
        '''成员ID'''
        return self._UserId

    @property
    def open_id(self):
        '''非企业成员的标识'''
        return self._OpenId

    @property
    def device_id(self):
        '''手机设备号'''
        return self._DeviceId

class WeComUserGetRes(WeComResponseBase):
    """### 读取成员 返回类 (TODO 未完全封装)
    文档地址 : https://work.weixin.qq.com/api/doc/90000/90135/90196
    """

    def __init__(self, params = {}):
        self._userid : str = ''
        self._name : str = ''
        self._mobile : str = ''
        self._avatar : str = ''
        super().__init__(params=params)
    
    @property
    def user_id(self):
        '''成员ID'''
        return self._userid

    @property
    def name(self):
        '''成员姓名'''
        return self._name

    @property
    def mobile(self):
        '''手机号码'''
        return self._mobile

    @property
    def avatar(self):
        '''头像url'''
        return self._avatar
