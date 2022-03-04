# Author      :  VEADoc
# Email       :  1126@veadoc.me
# FileName    :  department.py
# Create      :  2021-10-20 04:24:23
# Description :  企业微信 通讯录管理 - 部门管理 返回类
# Document    :  https://work.weixin.qq.com/api/doc/90000/90135/90204

from typing import List, Union
from . import WeComResponseBase
from ..utils import MultiFillClass



class DepartmentListItem(MultiFillClass):
    """部门详情
    """

    def __init__(self, params=...):
        self._id : int = None
        self._name : str = ''
        self._name_en : str = ''
        self._parentid : int = None
        self._order : int = None
        super().__init__(params=params)

    @property
    def id(self):
        '''部门ID'''
        return self._id

    @property
    def name(self):
        '''部门名称'''
        return self._name

    @property
    def name_en(self):
        '''部门英文名(官方已弃用)'''
        return self._name_en

    @property
    def parent_id(self):
        '''父部门ID 根部门此值为0'''
        return self._parentid
    
    @property
    def order(self):
        '''在父部门中的排序'''
        return self._order

class WeComDepartmentListRes(WeComResponseBase):
    """### 读取部门列表 返回类
    文档地址 : https://work.weixin.qq.com/api/doc/90000/90135/90196
    """

    def __init__(self, params):
        self._department: list = []
        super().__init__(params=params)

    @property
    def department(self):
        '''部门列表'''
        return [ DepartmentListItem(x) for x  in self._department]

    def get_parent_department(self,dept_id):
        """### [业务] 获取父级部门
        获取指定部门ID的父级部门"""
        res = [ x for x in self.department if x.parent_id == dept_id]
        if res.__len__():
            return res[0]

    def get_department(self,dept_id):
        """### [业务] 获取部门
        获取指定ID的部门"""
        res = [ x for x in self.department if x.id == dept_id]
        if res.__len__():
            return res[0]