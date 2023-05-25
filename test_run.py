# ----------------------------------------
#              创建姓名：十元        
#              创建时间：2021/2/17 下午10:23
#              更新时间：
#   run功能实现：
#   1： 执行方法，执行自动化测试


# ---------------------------------------
from tools import MyHTMLTestRunner
from tools.MyHTMLTestRunner import HTMLTestRunner
import pytest
import unittest
from cases.test_login import LoginCase
from tools.File_Path import REPORT_PATH

suit = unittest.TestSuite()
loader = unittest.TestLoader()
suit.addTest(loader.loadTestsFromTestCase(LoginCase))

with open(REPORT_PATH, 'wb') as  f:
    runner = MyHTMLTestRunner.HTMLTestRunner(
        stream=f,
        verbosity=2,
        title='登录测试',
        description='一些简单的描述信息',
        tester='十元')
    runner.run(suit)

if __name__ == '__main__':
    pytest.main()
