import unittest,json,time
from common.excel import Xl
from common.mysql import  Mysql
from common.httpre import Http
import os
from common.config import getsqlparam
from common.log import log
class Test(unittest.TestCase):
    xl = Xl("sheetok")
    def all_do(self,i):
        #读取excel数据
        log().info("开始读取excel数据")
        self.alists=self.xl.get_rows_values(i)
        self.url=self.alists[0]
        self.mothond = self.alists[1]
        print(self.alists[2])
        self.headers_value=eval(self.alists[2])
        print(type(self.headers_value))
        if self.headers_value==None:
            self.headers = None
        else:
            self.headers=self.headers_value
        self.data = json.dumps(eval(self.alists[3]))
        self.beforesql = self.alists[4]
        self.beforesql = self.beforesql .split(";")
        self.aftersql = self.alists[5]
        self.aftersql = self.aftersql.split(";")
        self.exp = json.loads(self.alists[6], strict=False)
        log().info("读取excel数据完毕")
        #sql准备
        log().info("开始准备sql数据")
        print(getsqlparam())
        self.sql=Mysql(host=getsqlparam()[0],password=getsqlparam()[2],db=getsqlparam()[3],user=getsqlparam()[1])
        for i in range(0, len(self.beforesql) - 1):
            self.sql.executedo(self.beforesql[i])
        self.sql.close()
        log().info("sql数据准备完毕")
        #执行用例
        log().info("开始执行测试")
        self.headers={"Content-Type":"application/json"}
        self.http=Http(self.url,self.mothond,self.headers,self.data)
        self.req=self.http.dohttp()
        log().info("测试结束")

        # sql删除
        log().info("开始删除sql数据")
        print(getsqlparam())
        self.sql = Mysql(host=getsqlparam()[0], password=getsqlparam()[2], db=getsqlparam()[3], user=getsqlparam()[1])
        for i in range(0, len(self.aftersql) - 1):
            self.sql.executedo(self.aftersql[i])
        self.sql.close()
        log().info("sql数据删除完毕")
        return self.req

    def test(self):
        for i in range(1,self.xl.get_rows()):
            log().info("======第"+str(i)+"条用例开始执行======")
            self.rq=self.all_do(i)
            print(self.rq.headers)
            print("这里是返回码啊")
            print(self.rq.status_code)
            print(self.req.text)
            self.assertEqual(self.rq.status_code,200,"返回码不是200")
            self.assertEqual(self.rq.json(), self.exp, "返回内容有问题")
            log().info("======第" + str(i) + "条用例执行完毕======")

if __name__=="__main__":
    unittest.main()







