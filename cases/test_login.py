# ----------------------------------------
#              创建姓名：十元

#              创建时间：2021/2/15 下午6:38
#   功能实现：
#   1：调用exceltools 读取测试数据
#   2：调用requesttools 执行登录用例
#   3：日志打印（需要添加打印日志）
#   4：测试结果回写
# ---------------------------------------


import unittest
from tools.ddt import ddt, data
from tools.Excel_Tools import Exceltool
from tools.Request_Tools import RequestsTool
from tools.File_Path import EXCEL_PATH, now
from tools.Config_Tools import Config_Tools
from tools.Log_Tools import mylog
rt = RequestsTool()
@ddt
class LoginCase(unittest.TestCase):
    # 获取 测试数据
    sheet_name = Config_Tools().get('Excel', 'sheet_login')
    datas = Exceltool(EXCEL_PATH, sheet_name).read_excel_obj()

    mylog.info("获取到登录全部测试数据，共" + str(len(datas)) + '条测试用例。')

    def werit_e(self, case_id, resule, tester):
        # 调用exceltoos函数
        we = Exceltool(EXCEL_PATH, Config_Tools().get('Excel', 'sheet_login'))
        we.Excel_Write(case_id + 1, 8, resule)
        we.Excel_Write(case_id + 1, 9, tester)
        we.Excel_Write(case_id + 1, 10, str(now))

    @data(*datas)
    def test_login(self, case_data):

        # 1准备数据
        data = eval(case_data.data)
        expected = eval(case_data.expected)
        # 2 打印日志 调用接口
        mylog.info('开始调用' + case_data.server + '接口,执行' + str(case_data.case_id) + '--' + case_data.description + '用例')
        response = rt.requests(url=case_data.url, json=data, request_mode=case_data.method)
        mylog.info('调用' + case_data.server + '接口完成,结果：' + str(response))
        # 3 比对结果

        try:
            # 可能出现错误的代码
            mylog.info('准备比对结果，实际结果结果《' + str(response) + '》,预期结果：' + str(expected))
            self.assertEqual(response, expected)
            mylog.info('测试用例' + str(case_data.case_id) + '--' + case_data.description + '通过')
            # print('测试用例' + str(case_data.case_id) + '通过,测试数据' + case_data.data)
            # 回写测试结果
            self.werit_e(case_data.case_id, '通过', '十元')

        except Exception as e:
            # 出现错误执行的代码
            mylog.error('测试用例' + str(case_data.case_id) + '--' + case_data.description + '不通过')
            mylog.error(e)
            self.werit_e(case_data.case_id, '通过', '十元')

            raise e
        else:
            # 没有错误执行的代码
            # mylog.info('测试用例' + str(case_data.case_id) + '--' + case_data.description + '通过')
            # print('测试用例' + str(case_data.case_id) + '通过,测试数据' + case_data.data)
            pass
        finally:
            # 有没有错误都执行的代码块
            pass
