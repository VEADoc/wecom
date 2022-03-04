# Author      :  VEADoc
# Email       :  1126@veadoc.me
# FileName    :  callback.py
# Create      :  2021-09-02 22:21:14
# Description :  企业微信回调数据模型

from enum import Enum
from typing import List
from ..utils import MultiFillClass


class WeComCallback(MultiFillClass):
    """回调模型"""

    def __init__(self, params={}) -> None:
        if params.get("xml"):
            params = params["xml"]

        self._FromUserName: str = ""  # 此事件该值固定为sys，表示该消息由系统生成
        self._ToUserName: str = ""  # 企业微信CorpID
        self._CreateTime: str = ""  # 消息创建时间时间戳 （整型）
        self._MsgType: str = ""  # 消息的类型，此时固定为event

        self._Event: str = ""
        self._ChangeType: str = ""
        super().__init__(params=params)

    @property
    def event(self):
        """回调事件"""
        return self._Event

    @property
    def change_type(self):
        """变更类型"""
        return self._ChangeType

    @property
    def from_username(self):
        """消息来源方"""
        return self._FromUserName
