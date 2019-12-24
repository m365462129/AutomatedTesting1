# -*- coding: UTF-8 -*-

# #--------------------路径
# import sys
# from os.path import dirname,abspath
# file_path = abspath(__file__)#获取当前文件的绝对路径
# print(file_path)
# print(dirname(file_path))#获取这个文件的上一级目录


# #--------------------导入的函数起别名
# from time import sleep as myselfsleep
# myselfsleep(2)
# print("1111111")


# #--------------------字符串操作
# print("0：name is " + "GG"+ ", age is " + str(26))
# print("1：name is %s, age is %d" %("bruce",30))
# print("2：name is {}, age is {}" .format("AI",30))
# print("3：name is {1}, age is {0}" .format(22,"MM"))
# print("4：name is {n}, age is {a}" .format(n="TT",a=25))


# #--------------------if else
# if False:
#     pass
# elif False:
#     pass
# else:
#     pass


# #--------------------list
# lists = [1,2,3,5,"f"]
# print(lists)
# print(lists[0])
# print(lists[4])
# print("最后一个元素："+ lists[-1])
# lists.append("u")#末尾添加元素
# lists.pop(0)#删除列表中的指定的下标元素


# #--------------------for
# for i in range(5):
#     print(str(i))

# for i in range(0,10,3):
#     print(str(i))

# test_list = {"1","P","KH"}
# for item in test_list:
#     print(item)


# #--------------------字典
# dicts = {"username":"zhangsan","password":123456}
# for k,v in dicts.items():
#     print("key:"+ str(k) + "  value:" + str(v))

# dicts.pop("username")#删除键


# #--------------------异常
# raise "111111111111111" #程序员主动抛出异常

# try:
#     print("开始异常测试")
#     open("abc.txt","r")
# except BaseException as msg:
#     print("-------------------------------------------------------------异常报错了")
#     print("异常信息:"+msg)
# finally:
#     print("不管异常，都会执行这里")