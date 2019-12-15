# -*- coding: UTF-8 -*-
import json
import csv
import codecs
from itertools import islice
from xml.dom.minidom import parse

#------------------------------------------------------
#读取XML文件
data =  parse("./myxml.xml")
root = data.documentElement
print(root.nodeName)
user_list = root.getElementsByTagName('login')
user = user_list[0]
print("账号:" +user.getAttribute("username") + "  密码:" + user.getAttribute("password"))
#------------------------------------------------------



#------------------------------------------------------
# #读取CSV文件
# data = csv.reader(codecs.open("./mycsv.csv","r","utf_8_sig"))
# user_list = []
# for line in islice(data,1,None):
#     user_list.append(line)

# print(user_list)
#------------------------------------------------------




#------------------------------------------------------
# #读取json文件
# with(open("./myjson.json","r")) as f:
#     data = f.read()

# user_list = json.loads(data)
# print(user_list)
#------------------------------------------------------




#------------------------------------------------------
# #读取txt文件
# with(open("./mytext.txt","r")) as user_file:
#     data = user_file.readlines()

# #格式化处理
# user_list = []
# for line in data:
#     user = line[:-1].split(":")
#     user_list.append(user)

# print(user_list)
#------------------------------------------------------