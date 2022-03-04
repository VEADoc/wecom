from enum import Enum
from typing import List, Union
from . import WeComResponseBase
from ..utils import MultiFillClass

def __get_zh_cn_field(item_list :List) -> str:
    item_list = item_list or []
    res = [x for x in item_list if x["lang"] == "zh_CN"]
    if not res:
        return ""
    return res[0]["text"]

class WeComGetTemplateDetail(WeComResponseBase):
    def __init__(self, params={}):
        """### 针对多语言进行了阉割"""
        self._template_names: list = []
        self._template_content: list = {}
        super().__init__(params=params)

    @property
    def template_name(self) -> str:
        """### 模版名
        这里仅返回 lang 为 zh_CN 的值
        """
        return __get_zh_cn_field(self._template_names)

    @property
    def template_content(self):
        """模版内容"""
        return _TemplateDetailContent(self._template_content)


class _TemplateDetailContent(MultiFillClass):
    """模版内容"""

    def __init__(self, params: Union[dict, str] = {}):
        self._controls: list = []
        super().__init__(params)

    @property
    def controls(self):
        """控件"""
        return [_TemplateDetailControls(x) for x in self._controls]


class _TemplateDetailControls(MultiFillClass):
    """模版控件"""

    def __init__(self, params: Union[dict, str] = {}):
        self._property: dict = {}
        self._config: dict = {}
        super().__init__(params)

    @property
    def property_(self):
        """控件属性"""
        return _TemplateDetailControlProperty(self._property)

    @property
    def config(self):
        """控件配置"""
        return _TemplateDetailControlConfig(self._config)


class ControlPropertyTypeEnum(Enum):
    """控件类型"""
    
    Unknown = '未知'
    Text = '文本'
    Textarea = '多行文本' 
    Number = '数字' 
    Money = '金额' 
    Date = '日期/日期+时间 '
    Selector = '单选/多选 '
    Contact = '成员/部门 '
    Tips = '说明文字' 
    File = '附件' 
    Table = '明细' 
    Attendance = '假勤控件' 
    Vacation = '请假控件' 
    Location = '位置' 
    RelatedApproval = '关联审批单' 
    Formula = '公式' 
    DateRange = '时长'

class _TemplateDetailControlProperty(MultiFillClass):
    """### 控件属性
    阉割了多语言 仅返回中文
    """

    def __init__(self, params: Union[dict, str] = {}):
        self._control: ControlPropertyTypeEnum = ControlPropertyTypeEnum.Unknown
        self._id: str = ""
        self._title: list = []
        self._placeholder: list = []
        self._require: int = None
        self._un_print: int = None
        super().__init__(params)

    @property
    def control(self):
        '''控件类型'''
        return self._control

    @property
    def id(self):
        '''控件ID'''
        return self._id

    @property
    def title(self):
        '''### 控件名
        仅返回 lang 为 zh_CN 
        '''
        return __get_zh_cn_field(self._title)

    @property
    def placeholder(self):
        '''### 控件占位文本
        仅返回 lang 为 zh_CN 
        '''
        return __get_zh_cn_field(self._placeholder)

    @property
    def require(self) -> bool:
        '''是否必填'''
        return self._require == 1

    @property
    def un_print(self):
        '''是否不参与打印'''
        return self._un_print == 1


class _TemplateDetailControlConfig(MultiFillClass):
    """### 控件配置
    TODO 未完全封装
    """

    def __init__(self, params: Union[dict, str] = {}):
        self._date: dict = {}
        self._selector: dict = {}
        self._contact: dict = {}
        self._table: dict = {}
        self._attendance: dict = {}
        self._vacation_list: dict = {}
        super().__init__(params)

    @property
    def date(self):
        """### 日期/日期+时间控件 配置"""
        return _ControlConfigDate(self._date)

    @property
    def contact(self):
        """### 成员/部门控件配置"""
        return _ControlConfigContact(self._contact)


class _ControlConfigContact(MultiFillClass):
    """### 成员/部门控件 配置

    """

    def __init__(self, params: Union[dict, str] = {}):
        self._type: str = ""
        self._mode: str = ""
        super().__init__(params)

    @property
    def type(self):
        """### 选择方式
        - single 单选
        - multi 多选
        """
        return self._type

    @property
    def mode(self):
        """### 选择对象
        - user 成员
        - department 部门
        """
        return self._mode


class _ControlConfigDate(MultiFillClass):
    """日期/日期+时间控件 配置"""

    def __init__(self, params: Union[dict, str] = {}):
        self._type: str = ""
        super().__init__(params)

    @property
    def type(self):
        """### 时间展示类型
        - day 日期
        - hour 日期+时间"""
        return self._type
