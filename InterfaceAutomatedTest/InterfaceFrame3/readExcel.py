import os
import a_helper as Helper
from xlrd import open_workbook

class readExcel():
    def get_xls(self, xls_name, sheet_name):
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


    def get_default_xls(self):
        return readExcel().get_xls(Helper.xls_name, Helper.sheet_name)


if __name__ == '__main__':
    print(readExcel().get_default_xls())