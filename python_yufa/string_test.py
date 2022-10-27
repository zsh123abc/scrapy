from ast import If
from math import fabs
import re




'''
def judge(s):
    for i in range(len(s)):
        if re.search('\d',s[i]) or re.search('[a-z]',s[i]):
            continue
        else:
            print("标识符不合法，不能以特殊字符开头,第%s个"%i)
            break
'''

'''
s="Zbc123"

num = 0
char = 0
other = 0
for i in range(len(s)):
    if re.match('[0-9]',s[i]):
        num+=1
        continue
    elif re.match('[a-z]',s[i]):
        char+=1
        continue
    else:
        other+=1  
        continue  
print("num:%s,char:%s,other:%s"%(num ,char,other))              
'''

'''
# python中变量名的命名规范：以字母或者_开头，只包含数字、字母、下划线
import re

names = ["abc", "_name", "age_", "name_age", "__sex__", "_____", "a#123", "a123", "123a", "a!"]

for name in names:
    mt = re.match("^[a-zA-Z_]+[a-zA-Z0-9_]*$", name)
    if mt:
        print("符合规范的变量名:%s" % name)
    else:
        print("不符合规范的变量名:%s" % name)
'''  
# # 假设163邮箱的地址规范为：4-20位数字、字母、下划线+@163.com
# import re

# # 假设163邮箱的地址规范为：4-20位数字、字母、下划线+@163.com
# email_list = [
#     'aaa@163.com',
#     'sjk_dsa123@163.com',
#     'dahujd%dsak@163.com',
#     'dsnakndnklandklnklndasklnladnkaslakldnklanklasndl@163.com',
#     'ahidfhaf@qq.com'
# ]

# for email in email_list:
#     mt = re.match(r"^[a-zA-Z0-9_]{4,20}@163\.com", email)
#     if mt:
#         print("规范的163邮箱：%s" % email)
#     else:
#         print("不规范的163邮箱：%s" % email)


#首先清楚手机号的规则
#1.都是数字 2.长度为11 3.第一位是1 4.第二位是35678中的一位
 
# pattern = "1[35678]\d{9}"
# phoneStr = "1823009222"

# if re.match('\d',phoneStr) and len(phoneStr)==11 and (phoneStr[0] == 1,4) and re.match('[3-8]',phoneStr[1]):
#     print('正确')
# else:
#     print('错误')    

# 匹配以hello开头的字符串
# re.match("hello", "hello world")
# # 查看匹配到的内容
# print(re.match("hello", "hello world").group())
# # 匹配以hello或者Hello开头的字符串
# re.match(r"[hH]ello", "Hello world").group()
 
# s=' This is a demo '
# # replace（） 用后面的替换前面的 
# print(s.replace(' ',''))

'''str_ = "You are the best!"
print(str_.upper())#把所有字符中的小写字母转换成大写字母
print(str_.lower())#把所有字符中的大写字母转换成小写字母'''

'''string="abc,a,c"
print(type(string))
fuhao=","
string=string.split(fuhao)
print(type(string))
for i in string:
    print(type(i))'''

# s = input('请输入一个字符串:')
# if len(s)<21:
#     # 冒号右边是输出格式，依次是用‘=’填充，’^'居中对齐，'20’输出的长度,顺序不能出错。
#     print('{:=^20}'.format(s))
# else:
#     print(s)

# a=0
# b=1
# while a<=100:
#     print(a,end=',')
#     a,b=b,a+b

'''import sys
sys.path.append("D:/anaconda_3520/lib/site-packages")#append 中写入想导入不同文件夹中的模块路径
import jieba
n = input('请输入一段话:')
str =""
# lcut() 可以成词的都分割开
ls = jieba.lcut(n)
print(ls)
for i in ls:
    str +=i
    # [::-1]：倒序输出，只能处理字符串
# print(str[::-1])
fanstr=str[::-1]

ls = jieba.lcut(fanstr)
print(ls)'''

 # 当不给split函数传递任何参数时，分隔符sep会采用任意形式的空白字符：空格、tab、换行、回车
string = "Python is good"
print(string.split())