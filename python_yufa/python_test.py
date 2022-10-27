from os import sep
import time
'''sum=sum(range(1,101))
print(sum)'''


'''# 1，
# x=1
# y=1
# print(x,y,end=' ')
# while True:
#     z=x+y
#     x=y
#     y=z
#     if z>100:
#         break
#     print(z,end=' ')

# 2，
# def fibo(n):
#     if n <= 1:
#         return n
#     elif n <= 11:
#         return (fibo(n - 1) + fibo(n - 2))


# m = 100
# for i in range(1, m):
#     if m <= 100:
#         print(fibo(i), end=" ")
#     else:
#         break

# 3,
# def fibo(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1  # 退出标识
# for n in fibo(11):
#     print (n,end=' ')

# 4,




# def fibo(n):

#     result_list = []
#     a, b = 0, 1
#     while n > 0:
#         result_list.append(b)
#         a, b = b, a + b
#         n -= 1
#     return result_list

# t1 = time.perf_counter()
# print(fibo(11))
# t2 = time.perf_counter()
# print("时间：%s"%(t2-t1))


# def f(x,l=[]):
#     for i in range(x):
#         l.append(i*i)
#     print(l)
# f(2)   
# f(3,[3,2,1])
# f(3)'''


a=1
b=10
print(*range(a,b,2),*range(b,a,-2),sep='->')


lst = []
for i in range(b,a-1,-1):
    if i%2==0:
        i=str(i)
        lst.append(i)
    else:
        i=str(i)
        lst.insert(0,i)   
res = '->'.join(lst)
print(res)    