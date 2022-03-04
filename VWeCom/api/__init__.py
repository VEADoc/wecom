import re
import requests
from typing import Union
from redis import StrictRedis
from urllib.parse import quote_plus
from requests.models import Response
from ..utils import _get_md5
from ..response import *
from ..response.service import WeComGetSuiteTokenRes, WeComGetProviderAccessTokenRes


_CORP_AGENT_ACCESS_TOKEN_CACHE_KEY = "CORP_AGENT_{CORP_ID}_{agent_secret_md5}"

_PROVIDER_ACCESS_TOKEN_CACHE_KEY = "PROVIDER_{CORP_ID}"

_SERVICE_SUITE_TICKET_CACHE_KEY = "SUITE_TICKET_{SUITE_ID}"

_SERVICE_SUITE_ACCESS_TOKEN_CACHE_KEY = "SUITE_ACCESS_TOKEN_{SUITE_ID}"


class _WeComMixinBase(object):
    """混入类 基类"""

    @property
    def _corp_agent_access_token_key(self):
        _common_data: dict = self._common_data()
        _common_data.update({"agent_secret_md5": _get_md5(self.agent_secret)})
        return _CORP_AGENT_ACCESS_TOKEN_CACHE_KEY.format_map(_common_data)

    @property
    def _provider_access_token_key(self):
        return _PROVIDER_ACCESS_TOKEN_CACHE_KEY.format_map(self._common_data())

    @property
    def _suite_ticket_key(self):
        return _SERVICE_SUITE_TICKET_CACHE_KEY.format_map(self._common_data())

    @property
    def _suite_access_token_key(self):
        return _SERVICE_SUITE_ACCESS_TOKEN_CACHE_KEY.format_map(self._common_data())


class _WeComTokenMixin(_WeComMixinBase):
    """企业微信相关 token  获取"""

    def _get_access_token_from_redis(self):
        """从缓存里获取 ACCESS_TOKEN"""
        if self._access_token_redis:
            res = self._access_token_redis.get(
                self._access_token_redis_key or self._corp_agent_access_token_key
            )
            return res

    def _set_access_token_to_redis(self, res: WeComGetAccessTokenRes):
        """设置 ACCESS_TOKEN 到 缓存"""
        self.access_token = res.access_token

        if not (self._access_token_redis and res.errcode == 0):
            return
        return self._access_token_redis.set(
            name=self._access_token_redis_key or self._corp_agent_access_token_key,
            value=res.access_token,
            ex=res.expires_in,
        )


class _WeComServiceTokenMixin(_WeComMixinBase):
    """企业微信服务商suite相关 token ticket 获取"""

    def _get_suite_access_token_from_redis(self):
        """从缓存中获取suite access token"""
        if self._access_token_redis:
            res = self._access_token_redis.get(self._suite_access_token_key)
            return res

    def _get_suite_access_token(self):
        """获取套件access_token"""
        func = getattr(self, "get_suit_token", None)
        if not func:
            raise RuntimeError("非服务商接口不可调用此接口")

        suite_ticket = self.suite_ticket

        if not suite_ticket:
            if not self._access_token_redis:
                raise RuntimeError("未传入suite_ticket 和 token redis")
            suite_ticket = self._access_token_redis.get(self._suite_ticket_key)
            if not suite_ticket:
                raise RuntimeError("未获取到缓存的 suite_ticket")
        res = func(self.suite_id, self.suite_secret, suite_ticket)
        return res

    def _set_suite_access_token(self, res: WeComGetSuiteTokenRes):
        """设置 SUITE_ACCESS_TOKEN 到缓存"""
        self.suite_access_token = res.suite_access_token
        if not (self._access_token_redis and res.errcode == None):
            return

        return self._access_token_redis.set(
            name=self._suite_access_token_key,
            value=res.suite_access_token,
            ex=res.expires_in,
        )


class _WeComProviderTokenMixin(_WeComMixinBase):
    """企业微信服务商 token  获取"""

    def _get_provider_access_token_from_redis(self):
        """从缓存中获取provider access token"""
        if self._access_token_redis:
            res = self._access_token_redis.get(self._provider_access_token_key)
            return res

    def _get_provider_access_token(self):
        """获取provider_access_token"""
        func = getattr(self, "get_provider_token", None)
        if not func:
            raise RuntimeError("非服务商接口不可调用此接口")
        res = func(self.corp_id, self.provider_secret)
        return res

    def _set_provider_access_token(self, res: WeComGetProviderAccessTokenRes):
        """设置 provider_ACCESS_TOKEN 到缓存"""

        self.provider_access_token = res.provider_access_token

        if not (self._access_token_redis and res.errcode == None):
            return

        return self._access_token_redis.set(
            name=self._provider_access_token_key,
            value=res.provider_access_token,
            ex=res.expires_in,
        )


class WeCom(_WeComTokenMixin, _WeComServiceTokenMixin, _WeComProviderTokenMixin):
    """企业微信"""

    def __init__(
        self,
        corp_id: str = "",
        # 自建调用参数
        agent_id: str = "",
        agent_secret: str = "",
        access_token: str = "",
        # 服务商调用参数
        provider_secret: str = "",
        provider_access_token: str = "",
        suite_id: str = "",
        suite_secret: str = "",
        suite_access_token: str = "",
        suite_ticket: str = "",
        # 缓存相关
        access_token_redis: StrictRedis = None,
        access_token_redis_key: str = "",
        **kwargs,
    ) -> None:
        """## 初始化参数
        - `corp_id`
        - `access_token_redis`
        - `access_token_redis_key` 建议废弃

        ### 自建开发模式
        - `agent_id`
        - `agent_secret`
        - `access_token` 可缓存取得

        ### 服务商模式
        - `provider_secret`
        - `provider_access_token` 可缓存取得
        - `suite_id`
        - `suite_secret`
        - `suite_access_token` 可缓存取得
        - `suite_ticket` 可缓存取得

        ### kwargs
        - `proxy` 请求代理 会入参到 requests
        """
        self.corp_id = corp_id
        self.agent_id = agent_id
        self.agent_secret = agent_secret
        self.access_token = access_token
        self.provider_secret = provider_secret
        self.provider_access_token = provider_access_token
        self.suite_id = suite_id
        self.suite_secret = suite_secret
        self.suite_access_token = suite_access_token
        self.suite_ticket = suite_ticket
        self._access_token_redis = access_token_redis
        self._access_token_redis_key = access_token_redis_key
        self.req: Response = None
        self.kwargs = kwargs

    def _common_data(self) -> dict:
        """收集公共参数"""
        return {
            "ACCESS_TOKEN": self.access_token,
            "CORP_ID": self.corp_id,
            "AGENT_SECRET": self.agent_secret,
            "SUITE_ID": self.suite_id,
            "SUITE_ACCESS_TOKEN": self.suite_access_token,
            "PROVIDER_ACCESS_TOKEN": self.provider_access_token,
        }

    def _do_request(
        self,
        url: str,
        method: str,
        query_params: dict = {},
        body_data: dict = {},
        **kwargs,
    ):
        """### 发送请求
        - `url` 接口地址
        - `method` GET / POST
        - `query_params` 查询参数
        - `body_data` 请求参数
        """
        method = method.upper()
        if method not in ["GET", "POST"]:
            raise RuntimeError("无效的请求类型")

        # query_params['debug'] = 1 # debug 参数 每分钟每接口不能超过5次 否则会有频率限制

        proxy = self.kwargs.get("proxy")

        for try_time in range(2):

            _common_data = self._common_data()
            if not _common_data["ACCESS_TOKEN"] and "{ACCESS_TOKEN}" in url:
                """从缓存里获取 ACCESS_TOKEN"""
                _common_data["ACCESS_TOKEN"] = self._get_access_token_from_redis()

            if not _common_data["SUITE_ACCESS_TOKEN"] and "{SUITE_ACCESS_TOKEN}" in url:
                """从缓存里获取 SUITE_ACCESS_TOKEN"""
                _common_data[
                    "SUITE_ACCESS_TOKEN"
                ] = self._get_suite_access_token_from_redis()

            if (
                not _common_data["PROVIDER_ACCESS_TOKEN"]
                and "{PROVIDER_ACCESS_TOKEN}" in url
            ):
                _common_data[
                    "PROVIDER_ACCESS_TOKEN"
                ] = self._get_provider_access_token_from_redis()

            _url = url.format_map(_common_data)
            # print(_url)
            # breakpoint()
            if query_params:
                query_string = "&".join(
                    [f"{key}={val}" for key, val in query_params.items()]
                )

                if (
                    not re.match(
                        r"^http(s)?://([a-zA-Z0-9\._\-]*)(/[a-zA-Z0-9_\-]*)*(?P<question>\?)?",
                        _url,
                    )
                    .groupdict()
                    .get("question")
                ):
                    _url += "?" + query_string
                else:
                    _url += "&" + query_string

            if method == "GET":
                self.req: Response = requests.get(_url, proxies=proxy)
            if method == "POST":
                self.req: Response = requests.post(_url, json=body_data, proxies=proxy)

            res = self.req.json()
            # print(res)
            if try_time == 0:
                errcode = res.get("errcode")
                if (
                    errcode in [40014, 42001] and "{ACCESS_TOKEN}" in url
                ):  # 不合法的access_token  	access_token已过期
                    """重新获取 access_token 后再进行下一轮循环"""
                    self._set_access_token_to_redis(self.get_access_token())
                    continue
                if errcode in [40014, 40082] and "{SUITE_ACCESS_TOKEN}" in url:
                    """重新获取 suite_acccess_token 并进行下一轮循环"""
                    self._set_suite_access_token(self._get_suite_access_token())
                    continue
                if errcode in [40014, 40082] and "{PROVIDER_ACCESS_TOKEN}" in url:
                    """重新获取 provider_access_token 并进行下一轮循环"""
                    self._set_provider_access_token(self._get_provider_access_token())
                    continue
            return res

    def get_access_token(self) -> WeComGetAccessTokenRes:
        """### 获取access_token

        文档地址 : https://work.weixin.qq.com/api/doc/90000/90135/91039
        """
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={CORP_ID}&corpsecret={AGENT_SECRET}"
        res = self._do_request(url, "GET")
        t = WeComGetAccessTokenRes(res)
        if t.errcode == 0:
            self.access_token = t.access_token
        return t

    def o_auth_url(self, redirect_uri, redirect_url="", state="STATE"):
        """### 构造网页授权链接
        - `redirect_uri` 授权后重定向的回调链接地址
            - 原样传入 这里会自行对 链接做 url 编码
        - `redirect_url` 重定向后再次重定向的地址`业务参数`
            - 原样传入 这里会自行对 链接做 url 编码 会以 redirect_url=的形式附在redirect_uri后面
        - `state` 重定向后会带上state参数

        文档地址 : https://work.weixin.qq.com/api/doc/90000/90135/91022
        """
        redirect_url_args = (
            ""
            if not redirect_url
            else f'{"" if "?" in redirect_uri else "?"}redirect_url={quote_plus(redirect_url)}'
        )
        redirect_uri += redirect_url_args
        url = f"https://open.weixin.qq.com/connect/oauth2/authorize?appid={self.corp_id}&redirect_uri={quote_plus(redirect_uri)}&response_type=code&scope=snsapi_base&state={state}#wechat_redirect"
        return url

    def o_auth_get_user_info(self, code) -> WeComGetUserInfoRes:
        """### 获取访问用户身份
        - `code` 通过成员授权获取到的code

        文档地址 : https://work.weixin.qq.com/api/doc/90000/90135/91023
        """

        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/getuserinfo?access_token={self.access_token}&code={code}"

        res = requests.get(url)

        return WeComGetUserInfoRes(res.json())

    def get_corp_jsapi_ticket(
        self, force_reflush=False
    ) -> Union[str, WeComJSApiTicketRes]:
        """获取JSAPI 票据
        文档地址 : https://open.work.weixin.qq.com/api/doc/90000/90136/90506
        """

        url = "https://qyapi.weixin.qq.com/cgi-bin/get_jsapi_ticket?access_token={ACCESS_TOKEN}"

        if not force_reflush:
            """优先检查缓存里有没有"""
            if self._access_token_redis is not None:
                ticket = self._access_token_redis.get(f"__CORP_JSAPI_TICKET__")
                if ticket:
                    return ticket

        rqes = self._do_request(url, "GET")
        res = WeComJSApiTicketRes(rqes)
        if res.errcode == 0 and self._access_token_redis is not None:
            set_res = self._access_token_redis.set(
                f"__CORP_JSAPI_TICKET__", res.ticket, ex=res.expires_in
            )
            return res.ticket
        return res

    def get_app_jsapi_ticket(
        self, force_reflush=False
    ) -> Union[str, WeComJSApiTicketRes]:
        """获取应用 JSAPI 票据
        文档地址 : https://open.work.weixin.qq.com/api/doc/90000/90136/90506
        """

        url = "https://qyapi.weixin.qq.com/cgi-bin/ticket/get?access_token={ACCESS_TOKEN}&type=agent_config"

        if not force_reflush:
            """优先检查缓存里有没有"""
            if self._access_token_redis is not None:
                ticket = self._access_token_redis.get(
                    f"__APP_{self.agent_id}_JSAPI_TICKET__"
                )
                if ticket:
                    return ticket

        rqes = self._do_request(url, "GET")
        res = WeComJSApiTicketRes(rqes)
        if res.errcode == 0 and self._access_token_redis is not None:
            set_res = self._access_token_redis.set(
                f"__APP_{self.agent_id}_JSAPI_TICKET__", res.ticket, ex=res.expires_in
            )
            return res.ticket
        return res
