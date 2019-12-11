import configparser,os
#项目所在路径，以便进行全局路径读取
allpath="E:/MyProject/my/"
def ini(section,option):
    con=configparser.ConfigParser()
    con.read(allpath+"API_test/config/config.ini")
    vaule=con.get(section,option)
    return vaule
def getsqlparam():
    host=ini("sql","host")
    user=ini("sql","user")
    password=ini("sql","password")
    db=ini("sql","db")
    port=ini("sql","port")
    return host,user,password,db
if __name__=="__main__":
    print(getsqlparam())