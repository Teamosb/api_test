# ----------------------------------------
#              创建姓名：十元        
#              创建时间：2021/2/16 下午11:52
#              更新时间：
# 功能实现：
#   1： 记录一些常用路径
#   2：
"""
case    加载路径下的测试用例
confs   拼接配置文件，进行读取
datas   拼接Excel文件进行截取，取值
logs    拼接日志文件，写入日志
reports 拼接报告文件，生成报告
"""
# ---------------------------------------
import os
import time
# 当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
# 获取根目录 os.path.dirname(__file__) 是当前目录
PATH = os.path.dirname(os.path.dirname(__file__))

# 测试数据路径
DATAS_PATH = os.path.join(PATH + '/', 'datas')
EXCEL_PATH = os.path.join(DATAS_PATH + '/', 'login.xlsx')
# EXCEL_PATH = "/Users/Usersteamo/PycharmProjects/api_test/datas/login.xlsx"

# 测试用例路径
CASES_PATH = os.path.join(PATH + '/' + 'cases')
LOGIN_PATH = os.path.join(CASES_PATH + '/', 'test_login.py')
# 配置文件路径
CONFIGS_PATH = os.path.join(PATH + '/', 'config')
CONF_PATH = os.path.join(CONFIGS_PATH + '/', 'conf.ini')
# 日志文件路径
LOGS_PATH = os.path.join(PATH + '/', 'logs')
LOG_PATH = os.path.join(LOGS_PATH + '/', 'log.log')
# 报告文件路径
REPORTS_PATH = os.path.join(PATH + '/', 'reports')
REPORT_NAME ='接口测试.html'
REPORT_PATH = os.path.join(REPORTS_PATH + '/'+now +REPORT_NAME)

if __name__ == '__main__':
    print(REPORT_PATH)
