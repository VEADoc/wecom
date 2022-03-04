# Author      :  VEADoc
# Email       :  1126@veadoc.me
# FileName    :  user.py
# Create      :  2021-09-04 21:23:26
# Description :  企业微信 通讯录管理 - 成员管理
# Document    :  https://work.weixin.qq.com/api/doc/90000/90135/90194


from . import WeCom
from ..response.user import WeComUserGetRes,WeComUserGetUserinfoRes,WeComUserListRes


class WeComUser(WeCom):
    """企业微信 通讯录管理 - 成员管理"""

    def list(self,department_id:int,fetch_child:bool = False):
        """### 获取部门成员详情

        - `department_id` 部门ID
        - `fetch_child` 是否递归获取子部门下面的成员

        文档地址 : https://open.work.weixin.qq.com/api/doc/90000/90135/90201
        """

        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/list?access_token={ACCESS_TOKEN}'

        query_data = {
            'department_id':department_id,
            'fetch_child':(0,1)[fetch_child==True]
        }

        res = self._do_request(url=url, method='GET', query_params=query_data)

        return WeComUserListRes(res)

    def get(self, userid:str):
        """### 读取成员

        在通讯录同步助手中此接口可以读取企业通讯录的所有成员的信息，
        
        而自建应用可以读取该应用设置的可见范围内的成员信息。
        
        - `userid`  成员的 userid

        文档地址 : https://work.weixin.qq.com/api/doc/90000/90135/90196
        """

        url = "https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={ACCESS_TOKEN}"

        query_data = {
            'userid': userid
        }
        res = self._do_request(url=url, method='GET', query_params=query_data)

        return WeComUserGetRes(res)

    def get_user_info(self,code):
        """### 获取访问用户身份
        身份验证 -> 扫码授权登录 -> 获取访问用户身份

        该接口用于根据code获取成员信息

        - `code` 通过成员授权获取到的code

        文档地址 : https://work.weixin.qq.com/api/doc/90000/90135/91437
        """

        url = "https://qyapi.weixin.qq.com/cgi-bin/user/getuserinfo?access_token={ACCESS_TOKEN}"

        query_data = {
            'code': code
        }
        res = self._do_request(url=url, method='GET', query_params=query_data)

        return WeComUserGetUserinfoRes(res)