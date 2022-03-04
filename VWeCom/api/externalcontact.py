# Author      :  VEADoc
# Email       :  1126@veadoc.me
# FileName    :  externalcontact.py
# Create      :  2021-08-28 21:43:40
# Description :  客户联系
# Document    :  https://open.work.weixin.qq.com/api/doc/90000/90135/92109
from datetime import datetime
from typing import List, Optional, Union
from . import WeCom
from ..response.externalcontact import (
    ExternalContactGetRes,
    ExternalContactListRes,
    ExternalContactGroupchatListRes,
    ExternalContactGroupchatGetRes,
    ExternalContactGroupchatStatisticRes,
    ExternalContactGetFollowUserListRes,
    ExternalContactGroupchatStatisticByDayRes
)

class WeComExternalContact(WeCom):
    """企业微信 客户联系"""

    def get_follow_user_list(self):
        """### 获取配置了客户联系功能的成员列表
        文档地址 : https://developer.work.weixin.qq.com/document/path/92571
        """
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_follow_user_list?access_token={ACCESS_TOKEN}"

        res = self._do_request(url=url,method='GET')
        return ExternalContactGetFollowUserListRes(res)

    def list(self,userid:str):
        """### 获取客户列表
        文档地址 : https://developer.work.weixin.qq.com/document/path/92113
        """
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/list?access_token={ACCESS_TOKEN}"
        query_data = {
            'userid':userid
        }
        res = self._do_request(url=url,method='GET',query_params=query_data)
        return ExternalContactListRes(res)

    def get(self, external_userid: str, cursor: str = ''):
        """### 获取客户详情
        过此接口，根据外部联系人的userid 拉取客户详情。

        - `external_userid` 外部联系人的`userid`，注意不是企业成员的帐号
        - `cursor`  	上次请求返回的`next_cursor`

        文档地址 : https://open.work.weixin.qq.com/api/doc/90000/90135/92114
        """

        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get?access_token={ACCESS_TOKEN}"

        query_data = {
            'external_userid': external_userid,
            'cursor': cursor
        }
        res = self._do_request(url=url, method='GET', query_params=query_data)
        return ExternalContactGetRes(res)

    def groupchat_list(self, status_filter: int = 0, owner_filter: list = [], cursor: str = '', limit: int = 10) -> ExternalContactGroupchatListRes:
        """### 获取客户群列表
        该接口用于获取配置过客户群管理的客户群列表。

        - `status_filter` 客户群跟进状态过滤。
            - 0  所有列表(即不过滤)[`默认`]
            - 1  离职待继承
            - 2  离职继承中
            - 3  离职继承完成
        - `owner_filter` 群主过滤 传入 userid 列表
        - `cursor` 用于分页查询的游标，字符串类型，由上一次调用返回，首次调用不填
        - `limit` 分页，预期请求的数据量，取值范围 1 ~ 1000

        文档地址 : https://open.work.weixin.qq.com/api/doc/90001/90143/93414
        """

        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/list?access_token={ACCESS_TOKEN}"

        biz_data = {
            "status_filter": status_filter,
            "owner_filter": {
                "userid_list": owner_filter
            },
            "cursor": cursor,
            "limit": limit
        }

        res = self._do_request(url=url, method='POST', body_data=biz_data)

        return ExternalContactGroupchatListRes(res)

    def groupchat_get(self, chat_id: str, need_name: bool = False):
        """### 获取客户群详情
        通过客户群ID，获取详情。包括群名、群成员列表、群成员入群时间、入群方式。

        - `chat_id` 客户群ID
        - `need_name` 是否需要返回群成员的名字
            - False 不返回 [`默认`]
            - True 返回

        文档地址 : https://open.work.weixin.qq.com/api/doc/90000/90135/92122
        """

        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/get?access_token={ACCESS_TOKEN}"

        biz_data = {
            "chat_id": chat_id,
            "need_name": (0, 1)[need_name]
        }

        res = self._do_request(url=url, method='POST', body_data=biz_data)

        return ExternalContactGroupchatGetRes(res)

    def groupchat_statistic(self, 
        begin_time: Union[int,datetime], 
        end_time: Optional[Union[int,datetime]] = None, 
        owner_filter:List[str] = [],
        order_by: int = 1,
        order_asc: int = 0,
        offset: int = 0,
        limit: int = 500):
        """### 获取「群聊数据统计」数据 (`按群主聚合`)
        获取指定日期的统计数据。注意，企业微信仅存储180天的数据。

        - `begin_time` 开始时间 可传时间戳或者datetime对象
        - `end_time` 截止时间 不填则为同开始时间
        - `owner_filter` 群主ID过滤
        - `order_by` 排序方式
            - `1` - 新增群的数量 (`默认`)
            - `2` - 群总数
            - `3` - 新增群人数
            - `4` - 群总人数
        - `order_asc` 是否升序
            - `0` - 否 (`默认`)
            - `1` - 是
        - `offset` 分页，偏移量, 默认为0
        - `limit` 分页，预期请求的数据量，默认为500，范围 [1,1000]

        文档地址 : https://open.work.weixin.qq.com/api/doc/90000/90135/92133
        """
        # breakpoint()
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/statistic?access_token={ACCESS_TOKEN}"
        get_timestamp = lambda t: int(datetime(t.year,t.month,day=t.day).timestamp())
        if isinstance(begin_time,datetime):
            begin_time = get_timestamp(begin_time)
        if not end_time:
            end_time = begin_time
        if isinstance(end_time,datetime):
            end_time = get_timestamp(end_time)


        biz_data = {
            "day_begin_time": begin_time,
            "day_end_time": end_time,
            "owner_filter": {
                "userid_list": owner_filter
            },
            "order_by": order_by,
            "order_asc": order_asc,
            "offset" : offset,
            "limit" : limit
        }

        # breakpoint()
        res = self._do_request(url=url, method='POST', body_data=biz_data)

        return ExternalContactGroupchatStatisticRes(res)

    def groupchat_statistic_by_day(self,
        begin_time: Union[int,datetime], 
        end_time: Optional[Union[int,datetime]] = None, 
        owner_filter:List[str] = []):
        """### 获取「群聊数据统计」数据 (`按自然日聚合`)
        获取指定日期的统计数据。注意，企业微信仅存储180天的数据。
        - `begin_time` 开始时间 可传时间戳或者datetime对象
        - `end_time` 截止时间 不填则为同开始时间
        - `owner_filter` 群主ID过滤

        文档地址 : https://open.work.weixin.qq.com/api/doc/90000/90135/92133
        """

        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/statistic_group_by_day?access_token={ACCESS_TOKEN}"

        if isinstance(begin_time,datetime):
            begin_time = int(begin_time.timestamp())
        if not end_time:
            end_time = begin_time
        if isinstance(end_time,datetime):
            end_time = int(end_time.timestamp())

        biz_data = {
            "day_begin_time": begin_time,
            "day_end_time": end_time,
            "owner_filter": {
                "userid_list": owner_filter
            }
        }

        res = self._do_request(url=url, method='POST', body_data=biz_data)

        return ExternalContactGroupchatStatisticByDayRes(res)

    