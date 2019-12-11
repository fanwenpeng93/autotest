import logging
import time
from common.config import allpath
def log():
    now=time.strftime("%Y%m%d%H%M%S", time.localtime())
    logPath = allpath+"/API_test/log/"+now+".log"
    FORMAT = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
    logging.basicConfig(level=logging.INFO,filename=logPath, format=FORMAT)
    return logging