import sys
from os.path import dirname,abspath
sys.path.append(dirname(dirname(abspath(__file__))))#将项目的目录加入到路径
print("--this path =" + str(sys.path))
from FileA.aa import classA#这时可以直接导入

aobj = classA("tom")
aobj.sayByeBye()

print("1111111111")



