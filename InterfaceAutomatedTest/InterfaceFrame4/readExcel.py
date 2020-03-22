import os
import a_helper as Helper
from xlrd import open_workbook
import ast

class readExcel():
    def __init__(self):
        xlsname = 'runtest.xlsx'
        sheetname = 'Sheet1'
        datalist = []
        xlsPath = os.path.join(Helper.project_abspath,xlsname)
        file = open_workbook(xlsPath)
        sheet = file.sheet_by_name(sheetname)
        nrows = sheet.nrows
        for i in range(nrows):
            if i > 0 :
                data = sheet.row_values(i)
                if(data[1] == 1):
                    Helper.test_case_dir = "./" + data[2]
                    Helper.test_case_file_name = data[3]
                    Helper.test_data_dir = data[4]
                    Helper.xls_name = data[5]
                    Helper.sheet_name = data[6]
                    Helper.report_dir = "./" + data[7] + "/"
                    Helper.isResultToHtml = data[8] == 1
                    Helper.isAutoSendEmail = data[9] == 1
                    return
                pass
            pass
        pass
        printText = "----你没有开启测试请检查{}文件的{}配置".format(xlsname,sheetname)
        print('\033[1;31m' + printText + '\033[0m')
    pass

    def get_default_xls(self):
        return readExcel().get_xls(Helper.xls_name, Helper.sheet_name)
    pass


    def get_xls(self, xls_name, sheet_name):
        # print("你要读取的Excel名称为：{}, Sheet名为：{}".format(xls_name,sheet_name))
        datalist = []
        xlsPath = os.path.join(Helper.project_abspath,Helper.test_data_dir,xls_name)
        file = open_workbook(xlsPath)
        sheet = file.sheet_by_name(sheet_name)
        nrows = sheet.nrows
        # print("exl配置的行数="+str(nrows))
        for i in range(nrows):
            if i > 0:
                datalist.append(sheet.row_values(i))
                # print(sheet.row_values(i))
        return datalist
    pass


if __name__ == '__main__':
    print(readExcel().get_default_xls())