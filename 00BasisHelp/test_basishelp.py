# -*- coding: UTF-8 -*-
#



# #------------------------------------------------------------自动截图
# driver.get_screenshot_as_file("./error_png.png")


# #------------------------------------------------------------鼠标事件
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
# driver = webdriver.Firefox()
# driver.implicitly_wait(10)
# driver.get("https://www.baidu.com/")
# setting_ele = driver.find_element_by_css_selector("a.pf:nth-child(8)")
# ActionChains(driver).move_to_element(setting_ele).perform()



# #------------------------------------------------------------1.隐形等待时间
# from selenium import webdriver
# from time import sleep
# driver = webdriver.Firefox()
# driver.implicitly_wait(10)                      #等待网页加载完成，可设置超时时间
# driver.get("https://www.baidu.com/")
# sleep(2)                                        #直接沉睡
# #------------------------------------------------------------2.显性等待时间
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Firefox()
# driver.get("https://baidu.com")
# #5秒内每间隔0.5秒检测一次，直到until的条件满足就跳出检测
# WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.ID,"kw")))
# ##WebDriverWait(driver, 5, 0.5).until_not(EC.presence_of_element_located((By.ID,"kw")))
# ##隐性等待和显性等待可以同时用，等待的最长时间取两者之中的较大者



# #------------------------------------------------------------路径
# import sys
# from os.path import dirname,abspath
# file_path = abspath(__file__)#获取当前文件的绝对路径
# print(file_path)
# print(dirname(file_path))#获取这个文件的上一级目录


# #------------------------------------------------------------list
# lists = [1,2,3,5,"f"]
# print(lists)
# print(lists[0])
# print(lists[4])
# print("最后一个元素："+ lists[-1])
# lists.append("u")#末尾添加元素
# lists.pop(0)#删除列表中的指定的下标元素


# #------------------------------------------------------------字符串操作
# print("0：name is " + "GG"+ ", age is " + str(26))
# print("1：name is %s, age is %d" %("bruce",30))
# print("2：name is {}, age is {}" .format("AI",30))
# print("3：name is {1}, age is {0}" .format(22,"MM"))
# print("4：name is {n}, age is {a}" .format(n="TT",a=25))


# #------------------------------------------------------------for
# for i in range(5):
#     print(str(i))

# for i in range(0,10,3):
#     print(str(i))

# test_list = {"1","P","KH"}
# for item in test_list:
#     print(item)


# #------------------------------------------------------------字典
# dicts = {"username":"zhangsan","password":123456}
# for k,v in dicts.items():
#     print("key:"+ str(k) + "  value:" + str(v))

# dicts.pop("username")#删除键


# #------------------------------------------------------------异常
# raise "111111111111111" #程序员主动抛出异常

# try:
#     print("开始异常测试")
#     open("abc.txt","r")
# except BaseException as msg:
#     print("--异常报错了")
#     print("异常信息:"+msg)
# finally:
#     print("不管异常，都会执行这里")


# #------------------------------------------------------------控制浏览器
# from selenium import webdriver
# driver = webdriver.Firefox()
# driver.implicitly_wait(10)        #隐性等待，等待网页加载完成，最长等10秒
# driver.back()						#浏览器返回
# driver.forward()					#浏览器前进
# driver.refresh()					#浏览器刷新
# driver.close()					#关闭当前窗口
# driver.quit()						#退出浏览器
# driver.set_window_size(300,300)   #设置浏览器窗口大小
# driver.maximize_window()          #设置浏览器窗口为最大尺寸


# #------------------------------------------------------------选择下拉框
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.select import Select
# driver = webdriver.Firefox()
# driver.implicitly_wait(10)
# driver.get("https://www.baidu.com/")
# setting_ele = driver.find_element_by_css_selector("a.pf:nth-child(8)")
# ActionChains(driver).move_to_element(setting_ele).perform()
# sleep(1)
# driver.find_element_by_css_selector(".setpref").click()
# sleep(1)
# sel_ele = driver.find_element_by_id("nr")
# sel_ele.click()
# sleep(1)
# Select(sel_ele).select_by_value("20")#1：选择值
# #Select(sel_ele).select_by_index(1):2：选择下标
# #Select(sel_ele).select_by_visible_text("每页显示20条"):3：选择文本


# #------------------------------------------------------------浏览器拖动条
# from selenium import webdriver
# from time import sleep
# driver = webdriver.Firefox()
# driver.get("https://www.hao123.com/")
# sleep(2)
# js = "window.scrollTo(100,450)"#js代码拖动条拖到一个位置
# driver.execute_script(js)


# #------------------------------------------------------------Cookie
# from selenium import webdriver
# from time import sleep
# driver = webdriver.Firefox()
# driver.get("https://www.baidu.com/")
# driver.add_cookie({"name":"key-aaa","value":"value-aaa"})#增加cookie
# # driver.add_cookie({"name":"name","value":"jack"})
# # driver.add_cookie({"name":"token","value":"xdclasseyJhbGciOiJIUzI1NiJ9"})
# # driver.delete_cookie("key","value")#删除一个cookie
# # driver.delete_all_cookies()#删除所有cookie
# cookieList = driver.get_cookies()
# for item in cookieList:#遍历
#     print(item["name"]+"=>"+item["value"])





















































# #------------------------------------------------------------确认框
# from selenium import webdriver
# driver = webdriver.Firefox()
# confirm_win = driver.switch_to_alert()  #切换到确认框. 
# confirm_win.send_keys("警告框提示语")   
# confirm_win.dismiss()				    #点击确认框取消按钮
# confirm_win.accept()				    #点击确认框确定按钮



# #------------------------------------------------------------if else
# if False:
#     pass
# elif False:
#     pass
# else:
#     pass



# #------------------------------------------------------------导入的函数起别名
# from time import sleep as myselfsleep
# myselfsleep(2)
# print("1111111")