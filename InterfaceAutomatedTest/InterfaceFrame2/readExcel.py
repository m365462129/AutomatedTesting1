
import os
import getpathInfo

from xlrd import open_workbook#第三方库读Excel
path = getpathInfo.get_Path()#该项目的绝对路径


class readExcel():
    def get_xls(self,xls_name,sheet_name):
        data_list = []
        xlsPath = os.path.join(path,"testFile",'case',xls_name)# 获取用例文件路径
        file = open_workbook(xlsPath)# 打开Excel
        sheet = file.sheet_by_name(sheet_name)#获得打开Excel的sheet
        nrows = sheet.nrows # 获取这个sheet内容行数
        for i in range(nrows):
            #如果这个Excel的这个sheet的第i行的第一列不等于case_name,说明这一行不是标题栏而是真实的数据，那么我们把这行的数据添加到cls[]
            if (sheet.row_values(i)[0] != u'case_name'):
                data_list.append(sheet.row_values(i))
        return data_list



if __name__ == "__main__":
    print(readExcel().get_xls('userCase.xlsx', 'login'))
    # print(readExcel().get_xls('userCase.xlsx', 'login')[0][1])
    # print(readExcel().get_xls('userCase.xlsx', 'login')[1][2])
    pass





