# autotest
接口自动化测试框架
本项目适合基本的接口自动化测试
【目录】
common：
config 配置文件读取
excel excel文件读取
httpre 发送请求的封装
log 日志封装
mysql 数据库封装
log：
日志存放
report：
测试报告存放
testcasedir：
测试用例读取执行
run：
执行测试

【使用】
1、配置python环境，安装相关的包
2、在excel文件中按照列名填写接口相关的信息
3、点击run文件的进行自动化测试
【注意】
1、excel文件中，SQL与SQL之间以分号（;）分割开

【不足】
1、复杂逻辑的接口测试未考虑中，后续完善
2、项目结构不佳，后续优化
