
from . import WeComModelBase

class OAApplyEventModel(WeComModelBase):
    """提交审批申请 模型"""

    def __init__(self) -> None:
        self._creator_userid : str = ''
        self._template_id : str = ''
        self._use_template_approver : int = None
        self._choose_department : int = None
        super().__init__()


    # TODO 未完成 暂时不要使用




    # "creator_userid": "WangXiaoMing",
    # "template_id": "3Tka1eD6v6JfzhDMqPd3aMkFdxqtJMc2ZRioeFXkaaa",
	# "use_template_approver":0,
	# "choose_department":2,
    # "approver": [
# 	"choose_department":2,
#     "approver": [
#         {
#             "attr": 2,
#             "userid": ["WuJunJie","WangXiaoMing"]
#         },
#         {
#             "attr": 1,
#             "userid": ["LiuXiaoGang"]
#         }
#     ],
# 	"notifyer":[ "WuJunJie","WangXiaoMing" ],
#     "notify_type" : 1,
#     "apply_data": {
#          "contents": [
#                 {
#                     "control": "Text",
#                     "id": "Text-15111111111",
#                     "value": {
#                         "text": "文本填写的内容"
#                     }
#                 }
#             ]
#     },
#     "summary_list": [
#         {
#             "summary_info": [{
#                 "text": "摘要第1行",
#                 "lang": "zh_CN"
#             }]
#         },
#         {
#             "summary_info": [{
#                 "text": "摘要第2行",
#                 "lang": "zh_CN"
#             }]
#         },
#         {
#             "summary_info": [{
#                 "text": "摘要第3行",
#                 "lang": "zh_CN"
#             }]
#         }
#     ]