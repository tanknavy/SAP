'''
CALL SAP multi-Thread
'''
from multiprocessing import Process,Pool
import threading,multiprocessing
import sys,os,time,random
from datetime import datetime
import logging, logging.handlers
from pyrfc import Connection
from R3P_LOGON import R3P_LOGON

def get_logger(now):
    #LOG_FILE = r'C:\\PycharmProjects\book_tool.log'
    LOG_FILE = 'e:/python/sap/log/sapconsole__' + now + '.txt'

    handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024 * 1024, backupCount=5, encoding='utf-8')
    fmt = '%(asctime)s - %(levelname)s - %(message)s'

    formatter = logging.Formatter(fmt)
    handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger

class lgtest():
    logging.basicConfig(filename='e:/python/sap/SAP_TEMP.log',format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level = logging.INFO,filemode='a',datefmt='%Y-%m-%d%I:%M:%S %p')
#lgtest()

now = datetime.now().strftime('%y%m%d%H%M%S')
f = open('e:/python/sap/log/saprfc_log_' + now + '.txt','w')
get_logger(now)


class SAP_LOGON():
    def __init__(self):
        ASHOST='10.1.45.18'
        CLIENT='300'
        #SYSNR='00'
        SYSNR = '01'
        USER='MY_TEST'
        PASSWD='12345678'
        self.conn = Connection(ashost=ASHOST, sysnr=SYSNR, client=CLIENT, user=USER, passwd=PASSWD)

# conn.call('BAPI_USER_GET_DETAIL',USERNAME='AC32_TEST')
# conn = Connection(user='AC32_TEST', passwd='teabrk88', ashost='10.1.45.12', sysnr='00', client='140')
c = SAP_LOGON()
r3p = R3P_LOGON()


def call_sap(conn,name): # concurrent call sap
    print('thread %s is running...' % threading.current_thread().name)
    print('-------%s-----------' % name)
    print(c.conn.call('BAPI_USER_GET_DETAIL', USERNAME=name))
    time.sleep(random.random() * 2)
    print(c.conn.call('STFC_CONNECTION', REQUTEXT=u'Hello SAP!'))

def call_sap2(): # concurrent call sap
    print('thread %s is running...' % threading.current_thread().name)
    #print('-------%s-----------' % name)
    #print(c.conn.call('BAPI_USER_GET_DETAIL', USERNAME=name))
    time.sleep(random.random() * 2)
    #print(c.conn.call('STFC_CONNECTION', REQUTEXT=u'Hello SAP!'),file=f) # 输出重定向到文件f
    print(r3p.conn.call('STFC_CONNECTION', REQUTEXT=u'Hello SAP!'), file=f)  # 输出重定向到文件f

for x in range(10):
#for user in open('user_300.txt'):
    #t = threading.Thread(target=call_sap,args=(c,str.strip(user)))
    t = threading.Thread(target=call_sap2)
    t.start()

    #threading.Thread(target=call_sap,args=(c,str.strip(user))).start()

    #t.join()
    #print('thread %s end...' % threading.current_thread().name)
#f.close()