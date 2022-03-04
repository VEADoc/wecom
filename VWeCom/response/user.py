# Author      :  VEADoc
# Email       :  1126@veadoc.me
# FileName    :  user.py
# Create      :  2021-09-04 21:25:52
# Description :  企业微信 通讯录管理 - 成员管理 返回类
# Document    :  https://work.weixin.qq.com/api/doc/90000/90135/90194

from typing import List, Union
from . import WeComResponseBase
from ..utils import MultiFillClass


class WeComUserGetRes(WeComResponseBase):
    """### 读取成员 返回类
    文档地址 : https://work.weixin.qq.com/api/doc/90000/90135/90196
    """

    def __init__(self, params):
        self._userid: str = ''
        self._name: str = ''
        self._alias :str = ''
        self._avatar :str = ''
        self._thumb_avatar :str = ''
        self._gender: int = 0
        self._mobile: str = ''
        self._email: str = ''
        self._department: List[int] = []
        self._main_department : int = 0
        self._order: List[int] = []
        self._position: str = ''
        self._is_leader_in_dept : List[int] = []
        self._open_userid : str =''
        self._address : str = ''
        self._telephone : str = ''
        self._qr_code : str =''
        self._status : int = 0
        self._external_position : str = ''
        # TODO 拓展信息 extra , 对外属性 external_profile 暂不进行封装
        super().__init__(params=params)

    @property
    def userid(self):
        '''成员ID'''
        return self._userid
    
    @property
    def name(self):
        '''成员名称'''
        return self._name
    
    @property
    def alias(self):
        '''别名'''
        return self._alias

    @property
    def avatar(self):
        '''头像url'''
        return self._avatar

    @property
    def thumb_avatar(self):
        '''头像缩略图 url'''
        return self._thumb_avatar

    @property
    def gender(self):
        '''### 性别
        - 0 未知
        - 1 男
        - 2 女
        '''
        return int(self._gender)
    
    @property
    def mobile(self):
        '''手机号码'''
        return self._mobile

    @property
    def email(self):
        '''邮箱地址'''
        return self._email
    
    @property
    def department(self):
        '''成员所属部门ID列表'''
        return self._department
    
    @property
    def order(self):
        '''部门内的排序值，越大越靠前'''
        return self._order
    
    @property
    def is_leader_in_dept(self):
        '''所在部门是否为上级'''
        return self._is_leader_in_dept

    @property
    def main_department(self):
        '''成员主部门'''
        return self._main_department
    
    @property
    def position(self):
        '''职务信息'''
        return self._position

    @property
    def external_position(self):
        '''对外职务信息'''
        return self._external_position

    @property
    def open_userid(self):
        '''open_userid'''
        return self._open_userid
    
    @property
    def address(self):
        '''地址'''
        return self._address
    
    @property
    def telephone(self):
        '''座机'''
        return self._telephone
    
    @property
    def qr_code(self):
        '''成员个人二维码'''
        return self._qr_code
    
    @property
    def status(self):
        '''### 成员状态
        - 1 已激活
        - 2 已禁用
        - 3 未激活
        - 5 已退出
        
        已激活代表已激活企业微信或已关注微工作台（原企业号）。未激活代表既未激活企业微信又未关注微工作台（原企业号）。
        '''
        return self._status


class WeComUserGetUserinfoRes(WeComResponseBase):
    """### 扫码授权解析 返回类
    文档地址 : https://work.weixin.qq.com/api/doc/90000/90135/91437
    """

    def __init__(self, params=...):
        self._UserId : str = ''
        self._OpenId : str = ''
        super().__init__(params=params)

    @property
    def userid(self):
        '''企业成员用户ID'''
        return self._UserId
    
    @property
    def openid(self):
        '''非企业成员 openid'''
        return self._OpenId

class WeComUserListRes(WeComResponseBase):

    def __init__(self, params=...):
        self._userlist : list = []
        super().__init__(params=params)
    
    @property
    def user_list(self):
        '''成员列表'''
        return [WeComUserGetRes(x) for x in self._userlist]

    
    def get_leaders(self,dept_id) -> List[WeComUserGetRes]:
        """### [业务] 获取部门里的上级
        `dept_id` 部门ID 由于用户可能在多部门中 所以需要传入 部门ID
        """

        res = []
        for x in self.user_list:
            for idx,dep in enumerate(x.department):
                if dep != dept_id:
                    continue
                if x.is_leader_in_dept[idx] == 1:
                    res.append(x)

        return res
