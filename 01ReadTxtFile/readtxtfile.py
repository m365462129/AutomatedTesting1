# -*- coding: UTF-8 -*-
#读取配置文件


#读取文件
with(open("./user_info.txt","r")) as user_file:
    data = user_file.readlines()

#格式化处理
user_list = []
for line in data:
    user = line[:-1].split(":")
    user_list.append(user)

print(user_list)