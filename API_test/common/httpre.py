import requests,os
from common.log import log
class Http:
    def __init__(self,url,mothond,headers,data):
        self.url=url
        self.mothond = mothond
        self.headers = headers
        self.data = data
    def get(self):
        req=requests.get(self.url,params=self.data,headers=self.headers)
        return req
    def post(self):
        req=requests.post(self.url,data=self.data,headers=self.headers)
        return req
    def dohttp(self):
        if self.mothond=="get":
            print("get方法")
            return self.get()
        elif self.mothond=="post":
            return self.post()
        else:
            log().warn("方法错误")
if __name__=="__main__":
    pass

