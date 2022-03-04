# Author      :  VEADoc
# Email       :  1126@veadoc.me
# FileName    :  msgaudit.py
# Create      :  2021-11-30 16:07:31
# Description :  会话存档相关接口
# Document    :  https://open.work.weixin.qq.com/api/doc/90000/90135/91360


from typing import List, Union
from . import WeComResponseBase
from ..utils import MultiFillClass


class MsgAuditGroupchatMember(MultiFillClass):

    def __init__(self, params: Union[dict, str] = ...):
        self._memberid: str = ''
        self._jointime: int = None
        super().__init__(params=params)

    @property
    def member_id(self):
        '''成员ID'''
        return self._memberid

    @property
    def join_time(self):
        '''入群时间'''
        return self._jointime


class WeComUserMsgAuditGroupchatRes(WeComResponseBase):
    """### 获取会话内容存档内部群信息 返回类
    文档地址 : https://open.work.weixin.qq.com/api/doc/90000/90135/92951
    """

    def __init__(self, params):
        self._roomname: str = ''
        self._creator: str = ''
        self._room_create_time: int = None
        self._notice: str = ''
        self._members: list = []
        super().__init__(params=params)

    @property
    def room_name(self):
        '''群聊名称'''
        return self._roomname

    @property
    def creator(self):
        '''创建人ID'''
        return self._creator

    @property
    def room_create_time(self):
        '''群聊创建时间'''
        return self._room_create_time

    @property
    def notice(self):
        '''群公告'''
        return self._notice

    @property
    def members(self):
        '''群成员'''
        return [MsgAuditGroupchatMember(x) for x in self._members]
