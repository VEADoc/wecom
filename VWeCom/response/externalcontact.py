# Author      :  VEADoc
# Email       :  1126@veadoc.me
# FileName    :  externalcontact.py
# Create      :  2021-08-28 21:43:40
# Description :  客户联系 返回类
# Document    :  https://open.work.weixin.qq.com/api/doc/90000/90135/92109

from typing import List, Union
from . import WeComResponseBase
from ..utils import MultiFillClass

# 太尼玛长了 去掉了前面的 WeCom

class ExternalContactDetailExternalProfileAttrItem(MultiFillClass):

    def __init__(self, params: Union[dict, str] = {}):
        self._value : str = ""
        self._url : str = ""
        self._title : str = ""
        self._appid : str = ""
        self._pagepath : str = ""
        super().__init__(params=params)

    @property
    def value(self):
        '''[仅文本类型] 文本内容'''
        return self._value

    @property
    def url(self):
        '''[仅网页类型] 连接'''
        return self._url

    @property
    def title(self):
        '''[仅网页、小程序类型] 网页/小程序标题'''
        return self._title

    @property
    def appid(self):
        '''[仅小程序类型] appid'''
        return self._appid

    @property
    def page_path(self):
        '''[仅小程序类型] 小程序路径'''
        return self._pagepath
        
class ExternalContactDetailExternalProfileAttr(MultiFillClass):
    """外部联系人详情 - 自定义展示信息- 属性列表"""

    def __init__(self, params: Union[dict, str] = {}):
        self._type : int = None
        self._name : str = ''
        self._text : dict = {}
        self._web : dict = {}
        self._miniprogram : dict = {}
        super().__init__(params=params)

    @property
    def type(self):
        '''### 属性类型
        
        - 0 文本
        - 1 网页
        - 2 小程序
        '''
        return self._type

    @property
    def name(self):
        '''属性名'''
        return self._name

    @property
    def text(self) -> ExternalContactDetailExternalProfileAttrItem:
        '''文本属性'''
        return ExternalContactDetailExternalProfileAttrItem(self._text)

    @property
    def web(self) -> ExternalContactDetailExternalProfileAttrItem:
        '''网页属性'''
        return ExternalContactDetailExternalProfileAttrItem(self._web)

    @property
    def miniprogram(self) -> ExternalContactDetailExternalProfileAttrItem:
        '''小程序属性'''
        return ExternalContactDetailExternalProfileAttrItem(self._miniprogram)

class ExternalContactDetailExternalProfile(MultiFillClass):
    """外部联系人详情 - 自定义展示信息"""

    def __init__(self, params: Union[dict, str] = {}):
        self._external_attr :List[dict] = {}
        super().__init__(params=params)

    @property
    def external_attr(self) -> List[ExternalContactDetailExternalProfileAttr]:
        '''属性列表'''
        return [ExternalContactDetailExternalProfileAttr(x) for x in self._external_attr]

class ExternalContactDetail(MultiFillClass):
    """外部联系人详情"""

    def __init__(self, params: Union[dict, str]):
        self._external_userid: str = ""
        self._name: str = ""
        self._avatar: str = ""
        self._type: int = 0
        self._gender: int = 0
        """仅微信用户有"""
        self._unionid : str = ""
        """仅企业微信用户有"""
        self._position : str = ""
        self._corp_name : str = ""
        self._corp_full_name : str = ""
        self._external_profile : dict = {}
        super().__init__(params=params)

    @property
    def external_userid(self):
        """外部联系人的userid"""
        return self._external_userid

    @property
    def name(self):
        """### 名称
        - `微信用户` 微信昵称
        - `企业微信用户` 对外展示的别名或实名
        """
        return self._name

    @property
    def type(self):
        """### 联系人类型
        - 1 微信用户
        - 2 企业微信用户
        """
        return self._type

    @property
    def avatar(self):
        """头像url"""
        return self._avatar

    @property
    def gender(self):
        """### 性别
        - 0 未知
        - 1 男性
        - 2 女性
        """
        return self._gender

    @property
    def union_id(self):
        '''[仅微信] union_id'''
        return self._unionid

    @property
    def position(self):
        '''[仅企业微信] 职位'''
        return self._position

    @property
    def corp_name(self):
        '''[仅企业微信] 企业简称'''
        return self._corp_name

    @property
    def corp_full_name(self):
        '''[仅企业微信] 企业全称'''
        return self._corp_full_name

    @property
    def external_profile(self) -> ExternalContactDetailExternalProfile:
        '''[仅企业微信] 自定义展示信息'''
        return ExternalContactDetailExternalProfile(self._external_profile)

class ExternalContactFollowUserTag(MultiFillClass):
    """跟进人标签信息"""

    def __init__(self, params: Union[dict, str]):
        self._group_name: str = ""
        self._tag_name: str = ""
        self._type: int = 0
        self._tag_id
        super().__init__(params=params)

    @property
    def group_name(self):
        """标签的分组名称"""
        return self._group_name

    @property
    def tag_name(self):
        """标签名"""
        return self._tag_name

    @property
    def tag_id(self):
        """标签ID"""
        return self._tag_id

    @property
    def type(self):
        """### 标签类型
        - 1 企业设置
        - 2 用户自定义
        - 3 规则组标签
        """
        return self._type


class ExternalContactFollowUser(MultiFillClass):
    """外部联系人 - 跟进人信息"""

    def __init__(self, params: Union[dict, str]):
        self._userid: str = ""
        self._remark: str = ""
        self._description: str = ""
        self._createtime: int = 0
        self._tags: list = []
        self._remark_mobiles: list = []
        self._add_way: int = 0
        self._oper_userid: str = ""
        super().__init__(params=params)

    @property
    def userid(self):
        """跟进人用户ID"""
        return self._userid

    @property
    def remark(self):
        """备注"""
        return self._remark

    @property
    def description(self):
        """描述"""
        return self._description

    @property
    def createtime(self):
        """该成员添加此外部联系人的时间"""
        return self._createtime

    @property
    def tags(self) -> List[ExternalContactFollowUserTag]:
        """标签信息"""
        return [ExternalContactFollowUserTag(x) for x in self._tags]

    @property
    def remark_mobiles(self):
        """该成员对客户备注的手机号"""
        return self._remark_mobiles

    @property
    def add_way(self):
        """### 客户来源
        - 0 	未知来源
        - 1  	扫描二维码
        - 2 	搜索手机号
        - 3 	名片分享
        - 4 	群聊
        - 5 	手机通讯录
        - 6 	微信联系人
        - 7 	来自微信的添加好友申请
        - 8 	安装第三方应用时自动添加的客服人员
        - 9 	搜索邮箱
        - 201 	内部成员共享
        - 202 	管理员/负责人分配
        """
        return self._add_way

    @property
    def oper_userid(self):
        """### 发起添加的userid
        - 如果成员主动添加，为成员的userid；
        - 如果是客户主动添加，则为客户的外部联系人userid；
        - 如果是内部成员共享/管理员分配，则为对应的成员/管理员userid
        """
        return self._oper_userid

class ExternalContactGetFollowUserListRes(WeComResponseBase):
    """### 获取配置了客户联系功能的成员列表 返回类
    文档地址 : https://developer.work.weixin.qq.com/document/path/92571
    """

    def __init__(self, params):
        self._follow_user = []
        super().__init__(params=params)

    @property
    def follow_user(self) -> List[str]:
        '''成员ID列表'''
        return self._follow_user

class ExternalContactListRes(WeComResponseBase):
    """### 获取客户列表 返回类
    文档地址 : https://developer.work.weixin.qq.com/document/path/92113
    """

    def __init__(self, params):
        self._external_userid = []
        super().__init__(params=params)

    @property
    def external_userid(self) -> List[str]:
        '''外部联系人的userid列表'''
        return self._external_userid



class ExternalContactGetRes(WeComResponseBase):
    """### 获取客户详情 返回类
    文档地址 : https://open.work.weixin.qq.com/api/doc/90000/90135/92114
    """

    def __init__(self, params):
        self._external_contact: dict = {}
        self._follow_user: list = []
        super().__init__(params=params)

    @property
    def external_contact(self) -> ExternalContactDetail:
        """外部联系人信息"""
        return ExternalContactDetail(self._external_contact)

    @property
    def follow_user(self) -> List[ExternalContactFollowUser]:
        """跟进人列表"""
        return [ExternalContactFollowUser(x) for x in self._follow_user]


class GroupchatListItem(MultiFillClass):
    """客户群聊item"""

    def __init__(self, params: Union[dict, str]):
        self._chat_id: str = ""
        self._status: int = 0
        super().__init__(params=params)

    @property
    def chat_id(self):
        """## 客户群ID"""
        return self._chat_id

    @property
    def status(self):
        """客户跟进状态"""
        return self._status


class ExternalContactGroupchatListRes(WeComResponseBase):
    """### 获取客户群列表 返回类
    文档地址 : https://open.work.weixin.qq.com/api/doc/90001/90143/93414
    """

    def __init__(self, params):
        self._group_chat_list: list = []
        self._next_cursor: str = ""
        super().__init__(params=params)

    @property
    def group_chat_list(self) -> List[GroupchatListItem]:
        """## 客户群聊列表"""
        return [GroupchatListItem(x) for x in self._group_chat_list]

    @property
    def next_cursor(self):
        """## 分页游标"""
        return self._next_cursor


class GroupchatMemberListItemInvitor(MultiFillClass):
    """### 客户群邀请人"""

    def __init__(self, params: Union[dict, str]):
        self._userid: str = ""
        super().__init__(params=params)

    @property
    def user_id(self):
        """邀请人userid"""
        return self._user_id


class GroupchatAdminListItem(GroupchatMemberListItemInvitor):
    """群聊管理员"""

    @property
    def user_id(self):
        """管理员 userid"""
        return self._user_id


class GroupchatMemberListItem(MultiFillClass):
    """### 客户群成员信息"""

    def __init__(self, params: Union[dict, str]):
        self._userid: str = ""
        self._unionid: str = ""
        self._type: int = 0
        self._join_time: int = 0
        self._join_scene: int = 0
        self._invitor: dict = {}
        self._group_nickname: str = ""
        self._name: str = ""
        super().__init__(params=params)

    @property
    def userid(self):
        """用户ID"""
        return self._userid

    @property
    def unionid(self):
        """微信开放平台唯一身份标识"""
        return self._unionid

    @property
    def type(self):
        """成员类型 1 - 企业成员 , 2 - 外部联系人"""
        return self._type

    @property
    def join_time(self):
        """入群时间"""
        return self._join_time

    @property
    def join_scene(self):
        """入群方式
        - 1  由群成员邀请入群（直接邀请入群）
        - 2  由群成员邀请入群（通过邀请链接入群）
        - 3  通过扫描群二维码入群
        """
        return self._join_scene

    @property
    def invitor(self) -> GroupchatMemberListItemInvitor:
        """邀请人"""
        return GroupchatMemberListItemInvitor(self._invitor)

    @property
    def group_nickname(self):
        """在群里的昵称"""
        return self._group_nickname

    @property
    def name(self):
        """名字
        - 如果是微信用户，则返回其在微信中设置的名字
        - 如果是企业微信联系人，则返回其设置对外展示的别名或实名"""
        return self._name


class GroupchatItem(MultiFillClass):
    """### 客户群详情"""

    def __init__(self, params: Union[dict, str]):
        self._chat_id: str = ""
        self._name: str = ""
        self._owner: str = ""
        self._create_time: int = 0
        self._notice: str = ""
        self._member_list: list = []
        self._admin_list: list = []
        super().__init__(params=params)

    @property
    def chat_id(self):
        """客户群ID"""
        return self._chat_id

    @property
    def name(self):
        """客户群名称"""
        return self._name

    @property
    def owner(self):
        """群主 userid"""
        return self._owner

    @property
    def create_time(self):
        """创建时间"""
        return self._create_time

    @property
    def notice(self):
        """群公告"""
        return self._notice

    @property
    def member_list(self) -> List[GroupchatMemberListItem]:
        """成员列表"""
        return [GroupchatMemberListItem(x) for x in (self._member_list or [])]

    @property
    def admin_list(self) -> List[GroupchatAdminListItem]:
        """管理员列表"""
        return [GroupchatAdminListItem(x) for x in (self._admin_list or [])]


class ExternalContactGroupchatGetRes(WeComResponseBase):
    """### 获取客户群详情 返回类
    文档地址 : https://open.work.weixin.qq.com/api/doc/90000/90135/92122
    """

    def __init__(self, params):
        self._group_chat: dict = {}
        super().__init__(params=params)

    @property
    def group_chat(self) -> GroupchatItem:
        """客户群详情"""
        return GroupchatItem(self._group_chat)


class GroupchatStatisticItemData(MultiFillClass):
    """群聊统计数据"""

    def __init__(self, params: Union[dict, str] = {}):
        self._new_chat_cnt: int = None
        self._chat_total: int = None
        self._chat_has_msg: int = None
        self._new_member_cnt: int = None
        self._member_total: int = None
        self._member_has_msg: int = None
        self._msg_total: int = None
        self._migrate_trainee_chat_cnt: int = None
        super().__init__(params=params)

    @property
    def new_chat_cnt(self):
        '''新增客户群数量'''
        return self._new_chat_cnt

    @property
    def chat_total(self):
        '''截至当天客户群总数量'''
        return self._chat_total

    @property
    def chat_has_msg(self):
        '''活跃客户群数量'''
        return self._chat_has_msg

    @property
    def new_member_cnt(self):
        '''客户群新增群人数'''
        return self._new_member_cnt

    @property
    def member_total(self):
        '''截至当天客户群总人数'''
        return self._member_total
    
    @property
    def member_has_msg(self):
        '''截至当天有发过消息的群成员数'''
        return self._member_has_msg

    @property
    def msg_total(self):
        '''截至当天客户群消息总数'''
        return self._msg_total

    @property
    def migrate_trainee_chat_cnt(self):
        '''截至当天新增迁移群数(仅教培行业返回)'''
        return self._migrate_trainee_chat_cnt
        

class ExternalContactGroupchatStatisticItem(MultiFillClass):
    """群聊统计数据项 按群主"""

    def __init__(self, params: Union[dict, str] = ...):
        self._owner: int = None
        self._data: GroupchatStatisticItemData = GroupchatStatisticItemData()
        super().__init__(params=params)

    @property
    def owner(self):
        '''群主ID'''
        return self._owner

    @property
    def data(self):
        '''统计数据'''
        return self._data


class ExternalContactGroupchatStatisticByDayItem(MultiFillClass):
    """群聊统计数据项 按日"""

    def __init__(self, params: Union[dict, str] = ...):
        self._stat_time: int = None
        self._data: GroupchatStatisticItemData = GroupchatStatisticItemData()
        super().__init__(params=params)

    @property
    def stat_time(self):
        '''统计时间'''
        return self._stat_time

    @property
    def data(self):
        '''统计数据'''
        return self._data
class ExternalContactGroupchatStatisticRes(WeComResponseBase):
    """### 「群聊数据统计」数据 (`按群主聚合`) 返回类
    文档地址 : https://open.work.weixin.qq.com/api/doc/90000/90135/92133
    """

    def __init__(self, params={}):
        self._items: list = []
        super().__init__(params=params)

    @property
    def items(self):
        """统计数据"""
        return [ExternalContactGroupchatStatisticItem(x) for x in self._items]


class ExternalContactGroupchatStatisticByDayRes(WeComResponseBase):
    """### 「群聊数据统计」数据 (`按自然日聚合`) 返回类
    文档地址 : https://open.work.weixin.qq.com/api/doc/90000/90135/92133
    """

    def __init__(self, params={}):
        self._items: list = []
        super().__init__(params=params)

    @property
    def items(self):
        """统计数据"""
        return [ExternalContactGroupchatStatisticByDayItem(x) for x in self._items]
