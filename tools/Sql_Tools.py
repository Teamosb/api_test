# ----------------------------------------
#              创建姓名：十元        
#              创建时间：2021/2/17 下午6:42
#              更新时间：
#   数据库功能实现：
#   1： 查所有 查1条 查指定
#   2：增
#   3：改
#   4：查
#   5: 查询受影响的行，提交 关闭 单独写函数提高复用性

# ---------------------------------------
import pymysql
from tools.Config_Tools import Config_Tools


class Sql_tools:
    def __init__(self):
        # 数据库连接
        self.connecter = pymysql.connect(
            host=Config_Tools().get('MYSQL', 'HOST'),
            user=Config_Tools().get('MYSQL', 'USER'),
            password=Config_Tools().get('MYSQL', 'PWD'),
            database=Config_Tools().get('MYSQL', 'DB'),
            port=int(Config_Tools().get('MYSQL', 'port')),
        )
        # 创建游标
        self.cursor = self.connecter.cursor()

    # def setup(self):
    #     # 每次开始要执行的语句
    #     pass
    #
    # def tearDown(self):
    #     # 每次结束要执行的语句 有问题
    #     self.commit()
    #     self.close()

    def select_count(self, sql):
        # 先查找受影响的数据
        return self.cursor.execute(sql)

    def commit(self):
        # 提交事务 关闭连接
        self.connecter.commit()

    def close(self):
        #关闭游标
        #关闭连接
        self.cursor.close()
        self.connecter.close()
    def insert(self,sql):
        # 插入调用 select_count函数
        #提交事务
        sql_result =self.select_count(sql)
        self.commit()
        return sql_result
    def delete(self,sql):
        # 删除调用 select_count函数
        # 提交事务
        sql_result= self.select_count(sql)
        self.commit()
        return sql_result
    def updata(self ,sql):
        # 修改调用 select_count函数
        # 提交事务
        sql_result=self.select_count(sql)
        self.commit()
        return sql_result
    def select_all(self, sql):
        # 调用select_count函数
        # 查询全量以元组套元组的形式返回
        self.select_count(sql)
        return self.cursor.fetchall()

    def select_one(self,sql):
        # 调用select_count函数
        # 查询一条以元组套元组的形式返回
        self.select_count(sql)
        return self.cursor.fetchone()

if __name__ == '__main__':
    sql_all = "SELECT  * from  cola_member   "
    sql_one = "select  * FROM  Pinyin p  where Station = '安塘1'"
    sql_delete = "DELETE FROM cola_member where id = '11111'"
    sql = "INSERT INTO cola_member(id, accountId, accountName, accountPWD, createTime,phoneNumber,accountType,holdMoney) VALUES ('11111','1',  '1',   '1',  '1', '1', '1','1')"
    sql_updata = "UPDATE  cola.cola_member  set accountPWD  ='queryuser1'  where id ='C04625B964634B8B93212D24DBC4C4F8'"

    do_sql = Sql_tools()
    # print(do_sql.updata(sql_updata))
    print(do_sql.select_all(sql_all))
    do_sql.close()

