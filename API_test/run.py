from testcasedir.testcase import Test
import unittest,os,time
from BeautifulReport import BeautifulReport
from common.config import getsqlparam

if __name__=="__main__":
    test_dir = './testcasedir'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    now = time.strftime("%Y%m%d%H%M%S", time.localtime())
    # 定义测试报告
    BeautifulReport(discover).report(filename='接口自动化测试报告'+now, description='测试用例', log_path='./report/')

