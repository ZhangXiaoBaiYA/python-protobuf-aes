# -*- coding:UTF-8 -*-
import requests

class HttpUtil:
    def __init__(self,base_url,platform):
        self.baseUrl = base_url
        self.header = {"TRADING_CHAIN_PLATFORM":platform,"content-type":"application/x-protobuf"}

    def request(self,req_url,text):
        """
        数据请求，这里使用post方式
        content-type:application/x-protobuf
        指定header,用于后端服务进行过滤请求
        """
        res = requests.post(self.baseUrl + req_url,text,headers = self.header)
        return res
