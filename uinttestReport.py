#----------------------------------------
#              创建姓名：十元        
#              创建时间：2021/5/12 下午11:02
#              更新时间：
#功能实现：
#   1： 
#   2：

#---------------------------------------

from unittestreport import TestRunner
import unittest
from cases.test_login import LoginCase
from tools.File_Path import REPORT_PATH

suit =unittest.TestSuite()
loader =unittest.TestLoader()
suit.addTest(loader.loadTestsFromTestCase(LoginCase))


runner = TestRunner(suit)
# 第三步：执行测试
runner.run()
