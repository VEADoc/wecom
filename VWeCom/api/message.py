# Author      :  VEADoc
# Email       :  1126@veadoc.me
# FileName    :  message.py
# Create      :  2021-09-06 17:40:44
# Description :  企业微信 消息推送 
# Document    :  具体看各自接口定义的文档



import json
from . import WeCom
from ..response.message import WeComSendAgentMessageRes
from ..model import AgentMessageModel

class WeComMessage(WeCom):
    """企业微信 消息推送"""

    def send(self,message_model:AgentMessageModel = None, message_dict :dict= {}) -> WeComSendAgentMessageRes:
        """### 发送应用消息 
        下面2个参数传入一个即可
        - `message_model` 消息模型 继承自 `AgentMessageModel` 的实例
        - `message_dict` 消息字典 按照文档构造的
        文档地址 : https://work.weixin.qq.com/api/doc/90000/90135/90236
        """

        url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={ACCESS_TOKEN}'
        biz_data = message_dict
        if not biz_data:
            biz_data = message_model.get_model()
            biz_data['agentid'] = self.agent_id

        res = self._do_request(url=url,method='POST',body_data=biz_data)
        return WeComSendAgentMessageRes(res)

    def update_template_card(self,message_model:AgentMessageModel = None, message_dict :dict= {}):
        """### 更新模版卡片消息
        下面2个参数传入一个即可
        - `message_model` 消息模型 继承自 `AgentMessageModel` 的实例
        - `message_dict` 消息字典 按照文档构造的
        文档地址 : https://open.work.weixin.qq.com/api/doc/90000/90135/94888
        """
        
        url = 'https://qyapi.weixin.qq.com/cgi-bin/message/update_template_card?access_token={ACCESS_TOKEN}'
        biz_data = message_dict
        if not biz_data:
            biz_data = message_model.get_model()
            biz_data['agentid'] = self.agent_id

        res = self._do_request(url=url,method='POST',body_data=biz_data)
        return WeComSendAgentMessageRes(res)
