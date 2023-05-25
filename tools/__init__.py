# ----------------------------------------
#              创建姓名：十元

#              创建时间：2020/9/16 11:32 下午


# ---------------------------------------
import openpyxl
class ExcelData:
    def __init__(self, zipObj):
        for item in zipObj:
            setattr(self, item[0], item[1])


class ReadExcel:
    def __init__(self, file_name, sheet_name):
        self.file_name = file_name  # 路径文件名
        self.sheet_name = sheet_name  # sheet 页
    #     self.wb = openpyxl.load_workbook(file_name)  # 工作空间 加载文件
    #     self.sheet = self.wb[sheet_name]  #工作空间加载sheet页
    #
    # def excel_rad_obj(self):
    #     def func(x):
    #         return x.value
    #     #list(self.sheet.rows)[0] 获取第一行为一个元组
    #     # map (func,元组) 依次获取元组中的值执行func
    #     #list(map(func,元组)) 获取到值转回成list
    #     head = list(map(func, list(self.sheet.rows)[0]))  # 头部信息
    #     datas = []  # 数据
    #     # list[1:]从索引1到最后一个
    #     for item in list(self.sheet.rows)[1:]:
    #         #依次获取每个单元格的值，并转换成list
    #         data = list(map(func, item))
    #         #将头部描述(字段名)和数据打包成一个个元组
    #         #并把元组的集合转换成list
    #         obj = list(zip(head, data))
    #
    #         excel_data = ExcelData(obj)
    #         datas.append(excel_data)
    #     return datas
    #
    # def Excel_Write(self, row, cloume, value):
    #     self.sheet.cell(row, cloume).value = value
    #     self.wb.save(self.file_name)
    #

if __name__ == '__main__':
    path = '/Users/teamo/PycharmProjects/Class02/Day17/datas/login.xlsx'
    # ed = ReadExcel(path, 'Sheet2').excel_rad_obj()
    #
    # print(ed)
