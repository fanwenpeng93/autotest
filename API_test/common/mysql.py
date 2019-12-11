import pymysql.cursors
from common.log import log
from common.config import getsqlparam
from common.config import ini
class Mysql:
    def __init__(self,host, user, password, db, charset='utf8'):
        self.conn = pymysql.connect(host=host,
                            user=user,
                            password=password,
                            db=db,
                            charset=charset,
                            cursorclass=pymysql.cursors.DictCursor)
    def executedo(self,sql):
        try:
            self.conn.cursor().execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            print("未执行")
        finally:
            pass
    def close(self):
        self.conn.close()

if __name__=="__main__":
    pass


