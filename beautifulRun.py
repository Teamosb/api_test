#----------------------------------------
#              创建姓名：十元        
#              创建时间：2021/5/12 下午10:44
#              更新时间：
#功能实现：
#   1： 
#   2：

#---------------------------------------


import unittest
from cases.test_login import LoginCase
from tools.File_Path import REPORT_PATH

suit =unittest.TestSuite()
loader =unittest.TestLoader()
suit.addTest(loader.loadTestsFromTestCase(LoginCase))


# br = BeautifulReport(suit)
# br.report("cms平台注册用例自动化", "cms_api_report.html",REPORT_PATH)
