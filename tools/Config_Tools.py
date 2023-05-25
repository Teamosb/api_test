# ----------------------------------------
#              创建姓名：十元        
#              创建时间：2021/2/16 下午11:50
#              更新时间：
# 功能实现：
#   1： 读取confing 文件夹下的conf.ini
#   2：
# super() 函数是用于调用父类(超类)的一个方法。
# super() 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。
# MRO 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表。

# ---------------------------------------
from configparser import ConfigParser
from tools.File_Path import CONF_PATH


class Config_Tools(ConfigParser):
    def __init__(self):
        super(Config_Tools, self).__init__()
        self.read(CONF_PATH, encoding='utf8')


config_tools = Config_Tools()

if __name__ == '__main__':
    print(Config_Tools().get('Excel', 'sheet_name_register'))
