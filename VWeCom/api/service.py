# Author      :  VEADoc
# Email       :  1126@veadoc.me
# FileName    :  service.py
# Create      :  2022-01-26 23:08:35
# Description :  服务商相关接口


from typing import List
from . import WeCom
from ..response.service import (
    WeComGetLoginInfoRes,
    WeComGetProviderAccessTokenRes,
    WeComGetSuiteTokenRes,
    WeComGetCustomizedAuthUrlRes,
    WeComGetPermanentCodeRes,
    WeComGetAuthInfoRes,
    WeComGetCorpTokenRes,
    WeComCorpidToOpenCorpidRes,
    WeComUseridToOpenUseridRes,
)


class WeComService(WeCom):
    """企业微信 服务商相关接口"""

    def get_provider_token(self, corpid="", provider_secret=""):
        """### 获取服务商凭证

        文档地址 https://developer.work.weixin.qq.com/document/path/91200
        """

        url = "https://qyapi.weixin.qq.com/cgi-bin/service/get_provider_token"

        body_data = {
            "corpid": corpid or self.corp_id,
            "provider_secret": provider_secret or self.provider_secret,
        }

        res = self._do_request(url, method="POST", body_data=body_data)

        return WeComGetProviderAccessTokenRes(res)

    def get_suit_token(self, suite_id="", suite_secret="", suite_ticket=""):
        """### 获取第三方应用凭证

        文档地址 https://developer.work.weixin.qq.com/document/path/90600
        """

        url = "https://qyapi.weixin.qq.com/cgi-bin/service/get_suite_token"

        body_data = {
            "suite_id": suite_id or self.suite_id,
            "suite_secret": suite_secret or self.suite_secret,
            "suite_ticket": suite_ticket or self.suite_ticket,
        }

        res = self._do_request(url, method="POST", body_data=body_data)

        return WeComGetSuiteTokenRes(res)

    def get_customized_auth_url(self, templateid_list: List[str], state: str):
        """### 获取带参授权链接

        文档地址 https://developer.work.weixin.qq.com/document/path/95436
        """

        url = "https://qyapi.weixin.qq.com/cgi-bin/service/get_customized_auth_url?provider_access_token={PROVIDER_ACCESS_TOKEN}"

        body_data = {"templateid_list": templateid_list, "state": state}

        res = self._do_request(url, method="POST", body_data=body_data)

        return WeComGetCustomizedAuthUrlRes(res)

    def get_permanent_code(self, auth_code):
        """### 获取企业永久授权码
        - `auth_code` 临时授权码

        文档地址 https://developer.work.weixin.qq.com/document/path/90603#14942
        """

        url = "https://qyapi.weixin.qq.com/cgi-bin/service/get_permanent_code?suite_access_token={SUITE_ACCESS_TOKEN}"

        body_data = {"auth_code": auth_code}

        res = self._do_request(url, method="POST", body_data=body_data)

        return WeComGetPermanentCodeRes(res)

    def get_auth_info(self, auth_corpid: str, permanent_code: str):
        """### 获取企业授权信息
        - `auth_corpid` 授权方corpid
        - `permanent_code` 	永久授权码

        文档地址 https://developer.work.weixin.qq.com/document/path/90604
        """

        url = "https://qyapi.weixin.qq.com/cgi-bin/service/get_auth_info?suite_access_token={SUITE_ACCESS_TOKEN}"

        body_data = {"auth_corpid": auth_corpid, "permanent_code": permanent_code}

        res = self._do_request(url, method="POST", body_data=body_data)

        return WeComGetAuthInfoRes(res)

    def get_corp_token(self, auth_corpid: str, permanent_code: str):
        """### 获取企业凭证
        - `auth_corpid` 授权方corpid
        - `permanent_code` 	永久授权码

        文档地址 https://developer.work.weixin.qq.com/document/path/90605
        """

        url = "https://qyapi.weixin.qq.com/cgi-bin/service/get_corp_token?suite_access_token={SUITE_ACCESS_TOKEN}"

        body_data = {"auth_corpid": auth_corpid, "permanent_code": permanent_code}

        res = self._do_request(url, method="POST", body_data=body_data)

        return WeComGetCorpTokenRes(res)

    def get_login_info(self, auth_code: str):
        """### 获取登录用户信息
        - `auth_code` 授权码

        文档地址 https://developer.work.weixin.qq.com/document/path/91125
        """

        url = "https://qyapi.weixin.qq.com/cgi-bin/service/get_login_info?access_token={PROVIDER_ACCESS_TOKEN}"

        body_data = {"auth_code": auth_code}

        res = self._do_request(url, method="POST", body_data=body_data)

        return WeComGetLoginInfoRes(res)

    def corpid_to_opencorpid(self, corpid: str):
        """### corpid转换
        - `corpid` 待获取的企业ID

        文档地址 https://developer.work.weixin.qq.com/document/path/95327
        """

        url = "https://qyapi.weixin.qq.com/cgi-bin/service/corpid_to_opencorpid?provider_access_token={PROVIDER_ACCESS_TOKEN}"

        body_data = {"corpid": corpid}

        res = self._do_request(url, method="POST", body_data=body_data)

        return WeComCorpidToOpenCorpidRes(res)

    def userid_to_openuserid(self, userid_list: List[str]):
        """### userid的转换
        - `userid_list` 获取到的成员ID

        文档地址 https://developer.work.weixin.qq.com/document/path/95327
        """

        url = "https://qyapi.weixin.qq.com/cgi-bin/batch/userid_to_openuserid?access_token={SUITE_ACCESS_TOKEN}"

        body_data = {"userid_list": userid_list}

        res = self._do_request(url, method="POST", body_data=body_data)

        return WeComUseridToOpenUseridRes(res)
