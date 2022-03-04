# Author      :  VEADoc
# Email       :  1126@veadoc.me
# FileName    :  department.py
# Create      :  2021-10-20 04:06:25
# Description :  部门相关接口
# Document    :  https://work.weixin.qq.com/api/doc/90000/90135/90204


from . import WeCom
from ..response.department import WeComDepartmentListRes


class WeComDepartment(WeCom):
    """企业微信 通讯录管理 - 部门管理"""

    def list(self,department_id:int = None):
        """### 获取部门列表

        - `department_id` 部门ID 不传则获取全量架构

        文档地址 : https://work.weixin.qq.com/api/doc/90000/90135/90208
        """

        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={ACCESS_TOKEN}&id=ID'

        query_data = {
            'department_id':department_id
        }

        res = self._do_request(url=url, method='GET', query_params=query_data)

        return WeComDepartmentListRes(res)
