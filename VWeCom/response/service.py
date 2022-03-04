# Author      :  VEADoc
# Email       :  1126@veadoc.me
# FileName    :  service.py
# Create      :  2022-01-27 00:04:35
# Description :  服务商相关接口返回类


from typing import List, Union
from enum import Enum

from . import WeComResponseBase,WeComGetAccessTokenRes
from ..utils import MultiFillClass


class WeComCorpTypeEnum(Enum):
    """企业认证类型"""

    unknown = "未知"

    verified = "认证号"
    unverified = "注册号"

class WeComUserTypeEnum(Enum):
    """登录用户的类型"""

    unknown = "未知"

    creator = '创建者'
    """`1` 创建者 """

    inner_admin = '内部系统管理员'
    """`2` 内部系统管理员 """

    outer_admin = '外部系统管理员'
    """`3` 外部系统管理员 """

    sub_admin = '分级管理员'
    """`4` 分级管理员 """

    member = '成员'
    """`5` 成员 """


class WeComGetProviderAccessTokenRes(WeComResponseBase):
    """### 获取服务商凭证 返回类"""

    def __init__(self, params=...):
        self._provider_access_token: str = ""
        self._expires_in: int = None
        super().__init__(params=params)

    @property
    def provider_access_token(self):
        """服务商token"""
        return self._provider_access_token

    @property
    def expires_in(self):
        """过期时间"""
        return self._expires_in


class WeComGetSuiteTokenRes(WeComResponseBase):
    """### 获取第三方应用凭证 返回类
    文档地址 : https://developer.work.weixin.qq.com/document/path/90600
    """

    def __init__(self, params=...):
        self._suite_access_token: str = ""
        self._expires_in: int = None
        super().__init__(params=params)

    @property
    def suite_access_token(self):
        """suite_access_token"""
        return self._suite_access_token

    @property
    def expires_in(self):
        """过期时间"""
        return self._expires_in


class WeComGetCustomizedAuthUrlRes(WeComResponseBase):
    """### 获取带参授权链接 返回类
    文档地址 https://developer.work.weixin.qq.com/document/path/95436
    """

    def __init__(self, params=...):
        self._qrcode_url: str = ""
        self._expires_in: int = None
        super().__init__(params)

    @property
    def qrcode_url(self):
        """### 二维码链接"""
        return self._qrcode_url

    @property
    def expires_in(self):
        """过期时间"""
        return self._expires_in


class DealerCorpInfo(MultiFillClass):
    """### 代理服务商企业信息。
    应用被代理后才有该信息"""

    def __init__(self, params: Union[dict, str] = ...):
        self._corpid: str = ""
        self._corp_name: str = ""
        super().__init__(params)

    @property
    def corp_id(self):
        """代理服务商 企业微信ID"""
        return self._corpid

    @property
    def corp_name(self):
        """代理服务商 企业微信名称"""
        return self._corp_name


class AuthCorpInfo(MultiFillClass):
    """授权方企业信息"""

    def __init__(self, params: Union[dict, str] = ...):
        self._corpid: str = ""
        self._corp_name: str = ""
        self._corp_full_name: str = ""
        self._corp_type: WeComCorpTypeEnum = WeComCorpTypeEnum.unknown
        self._corp_square_logo_url: str = ""
        self._corp_round_logo_url : str = ""
        self._corp_user_max: int = None
        self._subject_type: int = None
        self._verified_end_time: int = None
        self._corp_wxqrcode: str = ""
        self._corp_scale: str = ""
        self._corp_industry: str = ""
        self._corp_sub_industry: str = ""
        super().__init__(params)

    @property
    def corp_id(self):
        """企业微信id"""
        return self._corpid

    @property
    def corp_name(self):
        """企业简称"""
        return self._corp_name

    @property
    def corp_full_name(self):
        """### 企业主体名称
        仅认证或验证过的企业有"""
        return self._corp_full_name

    @property
    def corp_type(self):
        """企业认证类型"""
        return self._corp_type

    @property
    def corp_square_logo_url(self):
        """企业方型头像"""
        return self._corp_square_logo_url

    @property
    def corp_round_logo_url(self):
        '''企业圆形头像'''
        return self._corp_round_logo_url

    @property
    def corp_user_max(self):
        """企业用户规模"""
        return self._corp_user_max

    @property
    def subject_type(self):
        """### 企业类型
        - 1 `企业`
        - 2 `政府以及事业单位`
        - 3 `其他组织`
        - 4 `团队号`
        """
        return self._subject_type

    @property
    def verified_end_time(self):
        """认证到期时间"""
        return self._verified_end_time

    @property
    def corp_wxqrcode(self):
        """微信插件二维码"""
        return self._corp_wxqrcode

    @property
    def corp_scale(self):
        """企业规模"""
        return self._corp_scale

    @property
    def corp_industry(self):
        """企业所属行业"""
        return self._corp_industry

    @property
    def corp_sub_industry(self):
        """企业所属子行业"""
        return self._corp_sub_industry


class AgentPrivilege(MultiFillClass):
    """应用对应的权限"""

    def __init__(self, params: Union[dict, str] = ...):
        self._level : int = None
        self._allow_party : List[int] = []
        self._allow_user : List[str] = []
        self._allow_tag : List[int] = []
        self._extra_party : List[int] = []
        self._extra_user : List[str] = []
        self._extra_tag : List[int] = []
        super().__init__(params)

    @property
    def level(self):
        '''### 权限等级
        - 1 `通讯录基本信息只读`
        - 2 `通讯录全部信息只读`
        - 3 `通讯录全部信息读写`
        - 4 `单个基本信息只读`
        - 5 `通讯录全部信息只写`
        '''
        return self._level

    @property
    def allow_party(self):
        '''应用可见部门'''
        return self._allow_party

    @property
    def allow_user(self):
        '''应用可见成员'''
        return self._allow_user
    
    @property
    def allow_tag(self):
        '''应用可见标签'''
        return self._allow_tag

    @property
    def extra_party(self):
        '''额外可见部门'''
        return self._extra_party

    @property
    def extra_user(self):
        '''额外可见成员'''
        return self._extra_user
    
    @property
    def extra_tag(self):
        '''额外可见标签'''
        return self._extra_tag



class AgentSharedFrom(MultiFillClass):
    """共享了应用的企业信息"""

    def __init__(self, params: Union[dict, str] = ...):
        self._corpid : str = ''
        self._share_type : int = None
        super().__init__(params)

    @property
    def corp_id(self):
        '''企业微信ID'''
        return self._corpid

    @property
    def share_type(self):
        '''### 共享途径
        - 0 `企业互联`
        - 1 `上下游`
        '''
        return self._share_type

class AuthAgentInfo(MultiFillClass):
    """授权的应用信息"""

    def __init__(self, params: Union[dict, str] = ...):
        self._agentid: int = None
        self._name: str = ""
        self._round_logo_url: str = ""
        self._square_logo_url: str = ""
        self._appid: int = None
        self._auth_mode: int = None
        self._is_customized_app: bool = False
        self._privilege: dict = {}
        self._shared_from: dict = {}
        super().__init__(params)

    @property
    def agent_id(self):
        '''应用ID'''
        return self._agentid

    @property
    def name(self):
        '''应用名称'''
        return self._name

    @property
    def round_logo_url(self):
        '''应用圆型头像'''
        return self._round_logo_url

    @property
    def square_logo_url(self):
        '''应用方型头像'''
        return self._square_logo_url


    @property
    def appid(self):
        '''`弃用` 旧的多应用套件中的对应应用id'''
        return self._appid

    @property
    def auth_mode(self):
        '''### 授权模式
        - 0 `管理员授权`
        - 1 `成员授权`
        '''
        return self._auth_mode

    @property
    def is_customized_app(self):
        '''是否为代开发自建应用'''
        return self._is_customized_app

    @property
    def privilege(self):
        '''应用对应的权限'''
        return AgentPrivilege(self._privilege)

    @property
    def shared_from(self):
        '''### 共享了应用的企业信息
        仅当由企业互联或者上下游共享应用触发的安装时才返回'''
        return AgentSharedFrom(self._shared_from)



class AuthInfo(MultiFillClass):
    """授权信息"""

    def __init__(self, params: Union[dict, str] = ...):
        self._agent: list = []
        super().__init__(params)

    @property
    def agent(self):
        """授权的应用信息"""
        return [AuthAgentInfo(x) for x in self._agent]

class AuthUserInfo(MultiFillClass):
    """### 授权管理员的信息
    企业互联由上级企业共享第三方应用给下级时，不返回授权的管理员信息
    """
    def __init__(self, params: Union[dict, str] = ...):
        self._userid : str = ''
        self._open_userid : str = ''
        self._name: str = ''
        self._avatar : str = ''
        super().__init__(params)

    @property
    def userid(self):
        '''管理员用户ID'''
        return self._userid

    @property
    def open_userid(self):
        '''管理员open用户ID'''
        return self._open_userid

    @property
    def name(self):
        '''管理员名字'''
        return self._name

    @property
    def avatar(self):
        '''头像url'''
        return self._avatar

class RegisterCodeInfo(MultiFillClass):
    """推广二维码安装相关信息"""

    def __init__(self, params: Union[dict, str] = ...):
        self._register_code : str  = ''
        self._template_id : str = ''
        self._state : str = ''
        super().__init__(params)

    @property
    def register_code(self):
        '''注册码'''
        return self._register_code

    @property
    def template_id(self):
        '''推广包ID'''
        return self._template_id

    @property
    def state(self):
        '''仅当获取注册码指定该字段时才返回'''
        return self._state

class _WeComAuthInfoBase(WeComResponseBase):

    def __init__(self, params=...):
        self._dealer_corp_info: dict = {}
        self._auth_corp_info: dict = {}
        self._auth_info: dict = {}
        super().__init__(params)

    @property
    def dealer_corp_info(self):
        """### 代理服务商企业信息"""
        return DealerCorpInfo(self._dealer_corp_info)

    @property
    def auth_corp_info(self):
        """### 授权方企业信息"""
        return AuthCorpInfo(self._auth_corp_info)

    @property
    def auth_info(self):
        """### 授权信息"""
        return AuthInfo(self._auth_info)

class WeComGetPermanentCodeRes(_WeComAuthInfoBase):
    """### 获取企业永久授权码 返回类
    文档地址 https://developer.work.weixin.qq.com/document/path/90603#14942
    """

    def __init__(self, params=...):
        self._access_token: str = ""
        self._expires_in: int = None
        self._permanent_code: str = ""
        self._auth_user_info : dict = {}
        self._register_code_info : dict = {}
        self._state : str = ''
        super().__init__(params)

    @property
    def access_token(self):
        '''### 授权方（企业）access_token
        代开发自建应用安装时不返回。最长为512字节。'''
        return self._access_token

    @property
    def expires_in(self):
        '''### 授权方（企业）access_token超时时间（秒）。
        代开发自建应用安装时不返回。'''
        return self._expires_in

    @property
    def permanent_code(self):
        '''### 企业微信永久授权码
        最长为512字节'''
        return self._permanent_code

    @property
    def auth_user_info(self):
        '''### 授权管理员的信息
        企业互联由上级企业共享第三方应用给下级时，不返回授权的管理员信息
        '''
        return AuthUserInfo(self._auth_user_info)

    @property
    def register_code_info(self):
        '''### 推广二维码安装相关信息
        扫推广二维码安装时返回。
        注: 无论企业是否新注册，只要通过扫推广二维码安装，都会返回该字段'''
        return RegisterCodeInfo(self._register_code_info)

    @property
    def state(self):
        '''安装应用时，扫码或者授权链接中带的state值'''
        return self._state

class WeComGetAuthInfoRes(_WeComAuthInfoBase):
    """### 获取企业授权信息 返回类
    文档地址 https://developer.work.weixin.qq.com/document/path/90604
    """

class WeComGetCorpTokenRes(WeComGetAccessTokenRes):
    """### 获取企业凭证 返回类"""


class WeComUserInfoItem(MultiFillClass):
    """### 登录用户的信息"""

    def __init__(self, params: Union[dict, str] = {}):
        self._userid : str = ''
        self._open_userid : str = ''
        self._name : str = ''
        self._avatar : str = ''
        super().__init__(params)

    @property
    def userid(self):
        '''用户ID'''
        return self._userid

    @property
    def open_userid(self):
        '''对服务商唯一的ID'''
        return self._open_userid
    

    @property
    def name(self):
        '''用户名字'''
        return self._name

    @property
    def avatar(self):
        '''用户头像'''
        return self._avatar

class WeComGetLoginInfoRes(_WeComAuthInfoBase):
    """### 获取登录用户信息 返回类"""

    def __init__(self, params={}):
        self._usertype : WeComUserTypeEnum = WeComUserTypeEnum.unknown
        self._user_info : dict = {}
        super().__init__(params)
    
    @property
    def user_type(self):
        '''用户类型'''
        return self._usertype
    
    @property
    def user_info(self):
        '''用户信息'''
        return WeComUserInfoItem(self._user_info)

class WeComCorpidToOpenCorpidRes(WeComResponseBase):
    """### corpid转换  返回类"""

    def __init__(self, params={}):
        self._open_corpid : str = ''
        super().__init__(params)
    
    @property
    def open_corpid(self):
        '''该服务商第三方应用下的企业ID'''
        return self._open_corpid

class OpenUseridItem(MultiFillClass):
    """该服务商第三方应用下的成员ID和open userid"""

    def __init__(self, params: Union[dict, str] = {}):
        self._userid : str = ''
        self._open_userid : str = ''
        super().__init__(params)


    @property
    def userid(self):
        '''转换成功的userid'''
        return self._userid

    @property
    def open_userid(self):
        '''转换成功的userid对应的`该服务商应用下`的成员ID'''
        return self._open_userid

class WeComUseridToOpenUseridRes(WeComResponseBase):
    """### userid转换  返回类"""

    def __init__(self, params={}):
        self._open_userid_list : List[dict] = []
        self._invalid_userid_list : List[str] = []
        super().__init__(params)
    
    @property
    def open_userid_list(self):
        '''转换成功的userid对应的`该服务商应用下`的成员ID'''
        return [ OpenUseridItem(x) for x in self._open_userid_list ]

    @property
    def invalid_userid_list(self):
        '''无效的用户ID'''
        return self._invalid_userid_list
