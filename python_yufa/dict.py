
'''str=input('请输入字符串：')

a=set(str)#set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
count={}

#遍历集合a
for i in a:
    count[i]=str.count(i)#count()函数统计字符串str中的各个字符出现的次数。
#统计字典中最大的values
max1 = max(count.values())
# items()函数以列表返回可遍历的(键, 值)元组数组
data = list(count.items())
# 将元组以字母顺序对列表进行排序：
data.sort()
# 判断元组values是否等于最大值，满足则输出对应字母字符及出现次数
for i in data:
    if i[1] == max1:
        print(i[0], i[1])'''



'''name_dict = { 'mayun':'13309283335',

            'zhaolong':'18989227822',

            'zhangmin':'13382398921',

            'Gorge':'19833824743',

            'Jordan':'18807317878',

            'Curry':'15093488129',

            'Wade':'19282937665'}'''



'''name = input("输入人名查询号码")
print(name)
if name in name_list.keys():
    print(name_list[name])
       
else:
    print("查无此人")'''

'''#字典diicTXL和dicOther分别存储小明的通讯录和舍友通讯录信息，通信录中包括姓名、手机号和QQ号信息
# 字典中存放列表
dicTXL={'小新':['13913000001','18181220001'],
        '小亮':['13913000002','18191220002'],
        '小刚':['13913000003','18191220003']}
dicOther={'大刘':['13914000001','18191230001'],
          '大王':['13914000002','18191230002'],
          '大张':['13914000003','18191230003']}
#将字典dicOther合并到字典dicTXL中
dicTXL = dict(dicTXL, **dicOther)
print(dicTXL)
 
#dicWX字典存储同学的微信号
dicWX={'小新':'xx9907',
       '小刚':'gang1004',
       '大王':'jack_w',
       '大刘':'liu666'}

# 判断有微信号的就加入微信号，没有的则用手机号替代
for dicTxl_k,dicTxl_v in dicTXL.items():
    if dicTxl_k in dicWX:
        dicTxl_v.append(dicWX[dicTxl_k]) 
    else:
        dicTxl_v.append(dicTxl_v[0])

print(dicTXL)'''


'''dic_score={ '012':[90,94,85,54,68,75,71,21],
            '005':[8,75,21,65,89,97,25,75],
            '108':[87,54,78,25,14,98,67,57],
            '037':[45,87,54,82,95,91,57,32],
            '066':[95,67,51,48,98,92,80,39],
            '020':[85,81,65,97,35,62,71,84]}

print(dic_score)

pingjunfen = {}

for k ,v in dic_score.items():
    v_min = min(v)
    v_max = max(v)
    v_sum = sum(v)

    v_sum = v_sum - v_min - v_max # 去掉最高最低分
    
    v_avg = v_sum/(len(v)-2)
    pingjunfen[k]=v_avg
print(pingjunfen)

# reverse = True:降序，
# （key=lambda x: x[1]）x[1]是value值，指定规则就是按照value来排序
a1 = sorted(pingjunfen.items(), key=lambda x: x[1], reverse=True)
print(a1[0])'''




'''str = input('输入字符串：')
count = {'数字':0,'其他':0,"字母":0}
for i in str:
    if i.isalpha():
        count['字母'] += 1
    elif i.isdigit():
        count['数字'] += 1  
    else:
        count['其他'] += 1        

print(count)        '''



'''str = [6,17,81,3,29,12,51,16]
for i in range(len(str)): # 每一个数的下标
    if str[i]%3 == 0:
        str[i] = str[i]-2

print(str)'''


'''d1 = {'李阳':['音乐','读书','跑步'],
      '王天薇':['美食','诗歌','旅游'],
      '郭晓强':['编程','骑行','旅游','跑步'],
      '文雨非':['羽毛球','跑步','音乐','诗歌'],
      '郑菲菲':['美食','排球','舞蹈']}

new_dict = {}
for key,value in d1.items():
    for i in value:
        new_dict[i] = [key for key,value in d1.items() if i in value]
print(new_dict)'''



'''dic = {'k1':'v1','k2':'v2','k3':[11,22,33]}

for key in dic.keys():
    print(key, end=',')

for value in dic.values():
    print(value,end=",")   

for k,v in dic.items():
    print(k,v)    

dic['k4'] = 'v4'
print(dic)

dic['k1'] = 'alex'
print(dic)

k3_v = dic['k3']
dic['k3'].append('44') # append（）末尾插入
print(dic)

dic['k3'].insert(0,18) # insert（）指定位置插入
print(dic)

# del dic['k1']
# 与del函数不同，pop函数返回被删除项的值
print(dic.pop('k1'))
print(dic)

print(dic.pop('k5',"Node"))

print(dic['k2'])
print(dic.get('k2'))

print(dic.get('k6')) # get（）搜索不到就自动返回Node

dic2 = {'k1':'v111','a':'b'}
# 有相同的键会直接替换成 update 的值，有相同的键会直接替换成 update 的值
dic2.update({'k1':'v1','k2':'v2','k3':'v3'}) 
print(dic2)'''



'''# 组合嵌套
lis = [['k',['qwe',20,{'k1':['tt',3,'1']},89],'ab']]

# lis_tt =lis[0][1][2]['k1']
# lis_tt[0]=lis_tt[0].swapcase()
# print(lis)

lis_num = lis[0][1][2]['k1']
lis_num[1]=lis_num[1] = '100'
print(lis)'''



li = [1,2,3,'a','b',4,'c']
dic={}

if 'k1'not in dic:
    li2=[]
    for i in range(len(li)):
        if i % 2 == 1 and i!=0:
            li2.append(li[i]) 
    dic.setdefault('k1',li2)
else:
    if type(dic['k1']) == list:
        for i in range(len(li)):
            if i % 2 == 0 and i!=0:
                dic['k1'].append(li[i])       

# print(li2)
print(dic)    