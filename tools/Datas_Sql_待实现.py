#----------------------------------------
#              创建姓名：十元        
#              创建时间：2021/2/19 下午10:45
#              更新时间：
#功能实现：
#   1： 数据库中读取测试数据读取成对象形式
#   2：

#---------------------------------------

import pymysql
import pymysql
from tools.Config_Tools import Config_Tools
import pandas as pd


# class Sql_tools:
#     def __init__(self):
#         # 数据库连接
#         self.connecter = pymysql.connect(
#             host=Config_Tools().get('MYSQL', 'HOST'),
#             user=Config_Tools().get('MYSQL', 'USER'),
#             password=Config_Tools().get('MYSQL', 'PWD'),
#             database=Config_Tools().get('MYSQL', 'DB'),
#             port=int(Config_Tools().get('MYSQL', 'port')),
#         )
#         # 创建游标
#         self.cursor = self.connecter.cursor()



HOST='47.100.92.21'
port=3306
USER ='root'
PWD ='queryuser'
DB='cola'

def data_out_sql(DB, sql):
    conn = pymysql.connect(host=HOST,
                           port=port,
                           user=USER,
                           passwd=PWD,
                           db=DB,
                           charset='utf8')
    # 创建游标
    cursor = conn.cursor()
    # 执行sql语句
    sql ='SELECT  * from  cola_member  '
    cursor.execute(sql)
    # 调出数据
    data = cursor.fetchall()
    # cols为字段信息 例如(('factory_id', 253, None, 6, 6, 0, False), ('szDeviceId', 253, None, 30, 30, 0, False),('update_time', 7, None, 19, 19, 0, False))
    cols = cursor.description
    # 执行

    conn.commit()
    conn.close()
    # 将数据truple转换为DataFrame

    col = pd.DataFrame(columns={"id": "", "accountId": "", "accountName": "", "accountPWD": "",
                               "createTime": "", "phoneNumber": "", "accountType": "","holdMoney": ""
                               }, index=[0])




    for i in cols:
        col.append(i[0])
    data = list(map(list, data))
    data = pd.DataFrame(data, columns=col)

    print(data)
    return data


