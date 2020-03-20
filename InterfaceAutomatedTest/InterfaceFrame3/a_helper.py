# -*- coding: UTF-8 -*-


#---------------------------------------基本配置
test_dir = './test_case'     # 用例目录
test_case_file_name = 'test_general.py' #执行的测试用例文件命名规则
test_data_dir = 'test_data'
report_dir = './test_report/'# 报告目录
isResultToHtml = False        # 测试结果生成HTML
isAutoSendEmail = False       # 自动发送邮件

xls_name = 'userCase.xlsx'   #你要打开的xls名称
sheet_name = 'login'         #打开的xls中sheet名称

#---------------------------------------Email相关配置
mail_sender = "1032243432@qq.com"
mail_auth_code = "zrvhzhacmawtbbcc"
mail_smtpserver = "smtp.qq.com"
mail_receiverlist = ["1032243432@qq.com","365462129@qq.com"]


import os
project_abspath=os.path.split(os.path.realpath(__file__))[0]#当前文件的绝对路径
cur_run_case_index = 0#当前执行的用例数量
# import os
# if os.name == "nt":
#     os.system("")
# print('\033[1;31m' + text + '\033[0m')
# print('\033[1;33m' + text + '\033[0m')
# def print_error(text):
#     print('\033[1;31m' + text + '\033[0m')
# def print_warning(text):
#     print('\033[1;33m' + text + '\033[0m')

