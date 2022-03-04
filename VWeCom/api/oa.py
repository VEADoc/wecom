# Author      :  VEADoc
# Email       :  1126@veadoc.me
# FileName    :  oa.py
# Create      :  2022-01-20 19:32:13
# Description :  企业微信OA 接口 下方文档链接为审批 功能文档链接 进到页面后请左侧菜单栏选择要看的文档
# Document    :  https://developer.work.weixin.qq.com/document/path/91854


from . import WeCom
from ..model.oa import OAApplyEventModel
from ..response.oa import WeComGetTemplateDetail


class WeComOA(WeCom):
    """企业微信 OA"""

    def get_template_detail(self, template_id: str):
        """### 获取审批模板详情

        - `template_id` 模版的唯一标识

        文档地址 : https://developer.work.weixin.qq.com/document/path/91982
        """

        url = "https://qyapi.weixin.qq.com/cgi-bin/oa/gettemplatedetail?access_token={ACCESS_TOKEN}"

        query_data = {"template_id": template_id}

        res = self._do_request(url=url, method="POST", query_params=query_data)

        return WeComGetTemplateDetail(res)

    def apply_event(self,payload:dict = {} ,model : OAApplyEventModel = None):
        """### 提交审批申请
        下面2个参数 不可同时为空
        - `payload` 提交的数据
        - `model` 数据模型[暂不可用]

        文档地址 : https://developer.work.weixin.qq.com/document/path/91853
        """

        url = "https://qyapi.weixin.qq.com/cgi-bin/oa/applyevent?access_token={ACCESS_TOKEN}"

        body_data = payload

        res = self._do_request(url=url, method="POST", body_data=body_data)

        