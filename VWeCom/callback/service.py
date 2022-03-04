# Author      :  VEADoc
# Email       :  1126@veadoc.me
# FileName    :  service.py
# Create      :  2022-01-27 16:51:04
# Description :  服务商相关回调

from enum import Enum
from typing import List
from ..utils import MultiFillClass

class WeComServiceCallbackBase(MultiFillClass):
    """回调模型"""

    def __init__(self, params={}) -> None:
        if params.get("xml"):
            params = params["xml"]
        super().__init__(params=params)


class WeComServiceSuiteCallback(WeComServiceCallbackBase):

    def __init__(self, params={}) -> None:
        self._SuiteId : str = ""
        self._InfoType : str = ""
        self._TimeStamp : str = ""
        self._SuiteTicket : str = ""
        self._AuthCode : str = ""
        super().__init__(params)
    
    @property
    def suite_ticket(self):
        '''套件票据'''
        return self._SuiteTicket
    
    @property
    def timestamp(self):
        '''时间戳'''
        return int(self._TimeStamp or "0")
    
    @property
    def info_type(self):
        '''消息类型'''
        return self._InfoType
    
    @property
    def suite_id(self):
        '''套件ID 接口已不传'''
        return self._SuiteId
    
    @property
    def auth_code(self):
        '''授权码'''
        return self._AuthCode