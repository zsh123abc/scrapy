# -*- coding: UTF-8 -*-  

'''
# 导入fk_package包，实际上就是导入包下__init__.py文件
import my_package
# 导入fk_package包下的print_shape模块，
# 实际上就是导入fk_package目录下的print_shape.py
import my_package.print_shape
# 实际上就是导入fk_package包（模块）导入print_shape模块
from my_package import billing
# 导入fk_package包下的arithmetic_chart模块，
# 实际上就是导入fk_package目录下的arithmetic_chart.py
import my_package.arithmetic_chart
'''
# 包就是模块
# 这里导入my_package包，就是导入此包下面的__init__文件
# 而在__init__文件中，又导入了另外三个模块
# 所以只用导入my_package包就能用所有的模块

import sys
# import my_package

# sys.path.append() 把自定义包放到python可查询路径中，就可以无论在哪个盘都可以导入自定义包

sys.path.append('C:\\Users\\cwj')
from my_package import *
print(sys.path)
print(print_blank_triangle(5))


