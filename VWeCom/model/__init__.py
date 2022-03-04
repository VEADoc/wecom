from typing import Dict, List


class WeComModelBase(object):
    """请求模型"""

    def __init__(self) -> None:
        super().__init__()


    def load_params(self,data:dict):
        """加载参数"""
        # print(self.__dict__)
        for k,v in self.__dict__.items():
            print(k,v)
        return self

    def get_model(self) -> "List | Dict":
        """"""
