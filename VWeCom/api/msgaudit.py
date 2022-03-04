# Author      :  VEADoc
# Email       :  1126@veadoc.me
# FileName    :  msgaudit.py
# Create      :  2021-11-30 15:54:54
# Description :  会话存档相关接口
# Document    :  https://open.work.weixin.qq.com/api/doc/90000/90135/91360

from . import WeCom
from ..response.msgaudit import WeComUserMsgAuditGroupchatRes


class WeComMsgAudit(WeCom):
    """企业微信 会话内容存档"""

    def groupchat_get(self, roomid: str):
        """### 获取会话内容存档内部群信息
        企业可通过此接口，获取会话内容存档本企业的内部群信息，包括群名称、群主id、公告、群创建时间以及所有群成员的id与加入时间。
        - `roomid` 群聊ID

        文档地址 : https://open.work.weixin.qq.com/api/doc/90000/90135/92951
        """

        url = 'https://qyapi.weixin.qq.com/cgi-bin/msgaudit/groupchat/get?access_token={ACCESS_TOKEN}'

        body_data = {
            'roomid': roomid
        }

        res = self._do_request(url=url, method='POST', body_data=body_data)

        return WeComUserMsgAuditGroupchatRes(res)
