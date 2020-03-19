import os
from xlrd import open_workbook#第三方库读Excel
import configparser

path = os.path.split(os.path.realpath(__file__))[0]#该项目的绝对路径
config_path = os.path.join(path, 'config.ini')
config = configparser.ConfigParser()#调用外部的读取配置文件的方法
config.read(config_path, encoding='utf-8')

class Helper:
    def get_Path(self):
        return (os.path.split(os.path.realpath(__file__))[0])

    def get_xls(self,xls_name,sheet_name):
        data_list = []
        path = self.get_Path()
        xlsPath = os.path.join(path,"testFile",'case',xls_name)# 获取用例文件路径
        file = open_workbook(xlsPath)# 打开Excel
        sheet = file.sheet_by_name(sheet_name)#获得打开Excel的sheet
        nrows = sheet.nrows # 获取这个sheet内容行数
        for i in range(nrows):
            #如果这个Excel的这个sheet的第i行的第一列不等于case_name,说明这一行不是标题栏而是真实的数据，那么我们把这行的数据添加到cls[]
            if (sheet.row_values(i)[0] != u'case_name'):
                data_list.append(sheet.row_values(i))
        return data_list

    
    def get_http(self, name):
        return config.get('HTTP', name)
    def get_email(self, name):
        return config.get('EMAIL', name)
    def get_mysql(self, name):#写好，留以后备用。但是因为我们没有对数据库的操作，所以这个可以屏蔽掉
        return config.get('DATABASE', name)
    def get_Url(self):
        return (self.get_http('scheme') + '://' + self.get_http('baseurl') + ':8888' + '/login' + '?')

if __name__ == "__main__":
    # print('测试路径是否OK,路径为：', Helper().get_Path())
    # print(Helper().get_xls('userCase.xlsx', 'login'))
    # print('HTTP中的baseurl值为：', Helper().get_http('baseurl'))
    # print('EMAIL中的开关on_off值为：', Helper().get_email('on_off'))
    pass