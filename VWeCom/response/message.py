# Author      :  VEADoc
# Email       :  1126@veadoc.me
# FileName    :  message.py
# Create      :  2021-09-06 20:01:57
# Description :  企业微信 消息推送 返回类


from typing import List, Union
from . import WeComResponseBase
from ..utils import MultiFillClass


class WeComSendAgentMessageRes(WeComResponseBase):
    """发送应用消息接口返回值"""

    def __init__(self, params = {}):
        self._invaliduser : str = ''    # 无效的用户
        self._invalidparty: str = ''    # 无效的部门
        self._invalidtag  : str = ''    # 无效的标签
        self._response_code : str = ''  # 交互卡片 的 响应码
        super().__init__(params=params)

    @property
    def invalid_user(self):
        '''无效的用户'''
        return self._invaliduser

    @property
    def invalid_party(self):
        '''无效的部门'''
        return self._invalidparty

    @property
    def invalid_tag(self):
        '''无效的标签'''
        return self._invalidtag

    @property
    def response_code(self):
        '''交互消息响应码'''
        return self._response_code