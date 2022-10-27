'''def isUniqueThree1(astr: str) -> bool:
    nastr = str()
    for i in astr:
        if i not in nastr:
            nastr +=i
    return nastr ==astr

def isUniqueThree2(astr: str) -> bool:
    for s in range(len(astr)):
        for n in range(len(astr)):
            if s != n and astr[s] == astr[n]:
                return False
    return True

def isUnique(self, astr: str) -> bool:
        for s in range(len(self.astr)):
            for s2 in range(len(self.astr)):
                if s!=s2 and astr[s]==astr[s2]:
                    return False
        return True

def compare(a,b):
    if len(a)==len(b):
        lista=list(a)
        listb=list(b)
        lista.sort()
        listb.sort()
        print(lista==listb)
    else:
        print(False)

compare('abc','bca')'''


'''str = "               "
lens = 5
list_str = list(str)
for i in range(len(list_str)):
    if list_str[i] == ' ' and i<lens:
        list_str[i]='%20'
str = ''.join(list_str)
print(str)

S = "Mr John Smith    "
length = 13
str ='%20'.join(S[:length].split(" "))
print(str)'''


# odd = {}
# s = 'tactcoa'
# for ch in s:
#     if ch in odd.keys():
#         del odd[ch]
#     else:
#         odd[ch] = 0
# if len(odd.keys()) > 1:
#     print("False")
# else:
#     print("True")


# result = 0
# for c in s:
#     result ^= 1<< ord(c)
# print(result & (result - 1) == 0)

# import re


# s = 'II'
# a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
# ans = 0
# k1 = ''
# for k2 in a.keys():
#     k1 = k2
# for i,x in enumerate(s):
#     if re.match(r"[%s-%d]"%(a[x],a[k1]),x):
#         if i<len(s)-1 and a[x]<a[s[i+1]]:
#             ans = ans - a[s[i]]    
#         else:
#             ans = ans + a[s[i]]      
#     else:
#         if ans == 0:
#             print("输入错误，不是罗马数字") 
#             break            
# print(ans)



# strs = ["qflower", "flow", "flight"]

# if not strs:
#     print(" ")

# s1 = min(strs)
# s2 = max(strs)
# for i, x in enumerate(s1):
#     if x != s2[i]:
#         print(s2[:i])
#         break
# print(s1)



# nums = [2,7,11,15]
# target = 9

# for i,x in enumerate(nums):
#     if nums[i+1] +x == target:
#         print([i,i+1])
#         break


# x = -1
# # x2 = str(x)[::-1]
# # x2 = int(x2)
# # print(x==x2)

# print(x>0 and str(x)[::-1] == str(x))



# s = "())"

# if '{}' in s or '()' in s or '[]' in s:
#         s = s.replace('{}', '')
#         s = s.replace('[]', '')
#         s = s.replace('()', '')
# print(s =="")

# nums = [0,1,2,2,3,0,4,2]
# val = 2
# j=len(nums)
# for i in range(j-1,-1,-1):
#     if nums[i]==val:
#         nums.pop(i) 
# print(nums)        


# s = "barfoothefoobarman"
# words = ["foo","bar"]
# for i in range(len(words)-1 , 0 , -1):
#         words=words+words[i]
#         words+=' '
#         index=s.find(words)


# class Solution:
#     def search(self, nums: list[int], target: int) -> int:
#         left, right = 0, len(nums) - 1
        
#         while left <= right:
#             middle = (left + right) // 2

#             if nums[middle] < target:
#                 left = middle + 1
#             elif nums[middle] > target:
#                 right = middle - 1
#             else:
#                 return middle
#         return -1

# s = Solution()
# nums = [-1,0,3,5,9,12]
# target = 9
# index=s.search(nums,target)
# print(index)


# str_list=["h","e","l","l","o"]
# l = 0
# r = len(str_list)-1
# while l<r:
#     str_list[l],str_list[r] = str_list[r],str_list[l]
#     l+=1
#     r-=1
# print(str_list)

# s = "abcdefg"
# k = 2


# p = 0
# while p < len(s):
#     p2 = p + k

#     # s[:p], 0-p 
#     # s[p: p2][::-1], p-p2的所有元素进行反转 
#     # s[p2:], p2-字符串的最后
#     s = s[:p] + s[p: p2][::-1] + s[p2:]
#     # 在跳2k个下标
#     p = p + 2 * k
# print(s)



# s = "We are happy"
# s_list=list(s)

# str ='%20'.join(s.split(" "))
# print(str)        

# s = "the sky is blue"
# s_list=list(s.split(" "))
# l = []
# for i in range(len(s_list)-1,-1,-1):
#     l.append(s_list[i])
    
# print(l)    
# s = "We are happy"
# counter = s.count(' ')
        
# res = list(s)
# # 每碰到一个空格就多拓展两个格子，1 + 2 = 3个位置存’%20‘
# res.extend([' '] * counter * 2)
        
# # 原始字符串的末尾，拓展后的末尾
# left, right = len(s) - 1, len(res) - 1
        
# while left >= 0:
#     if res[left] != ' ':
#         res[right] = res[left]
#         right -= 1
#     else:
#         # [right - 2, right), 左闭右开
#         res[right - 2: right + 1] = '%20'
#         right -= 3
#     left -= 1
# j=''.join(res)
# print(j)


# class Solution:
#     def reverseLeftWords(self, s: str, n: int) -> str:
#         def reverse_sub(lst, left, right):
#             while left < right:
#                 lst[left],lst[right] = lst[right],lst[left]
#                 left+=1
#                 right-=1

#         s_list=list(s)
#         end = len(s_list)-1

#         reverse_sub(s_list,0,n-1)        
#         reverse_sub(s_list,n,end)        
#         reverse_sub(s_list,0,end)
#         str="".join(s_list)
#         print(str)        

# sol = Solution()
# s = "abcdefg"
# k = 2
# sol.reverseLeftWords(s,k)        


# haystack = "hello"
# needle = "ll" 
# # 输出: 2
# m,n = len(haystack),len(needle)
# for i in range(m):
#     if haystack[i:i+n]==needle:
#         print(i ,end="")



# nums = [3,2,2,3]
# val = 3
# l=0
# r=len(nums)-1
# while l < r:
#     while (l<r and nums[l]!=val):
#         l+=1
#     while (l<r and nums[r]==val):
#         r-=1
#     nums[l],nums[r] = nums[r],nums[l]        
# print(nums)



# nums = [8,1,2,2,3]
# n = 0
# new_nums = []
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if nums[i] >nums[j]:
#             n+=1
#     new_nums.append(n)
#     n = 0
# print(new_nums)    

# 把所有的数据赋值到res
# res = nums[:]
# # 创建一个空字典
# hash = dict()
# # 给res排序，排序后，元素的下标就是小于当前数字的数
# res.sort()
# # 循环取出res的数据和对应的下标
# for i,num in enumerate(res):
#     # 遇到了相同的数字就不需要重复更新了
#     if num not in hash.keys():
#         # 把数字对应的下标存进字典
#         hash[num]=i
# # 循环取出nums的数据和对应的下标
# for i,num in enumerate(nums):
#     # 把字典中数据对应的下标存进res里
#     res[i]=hash[num]

# print(res)            



# arr = [0,3,2,1]
# l = 0
# r = len(arr)-1
# # 左指针在迭代后不能超过数组长度 并且 l比l+1小
# while l<len(arr)-1 and arr[l]<arr[l+1]:
#     # 迭代l，从前往后移
#     l+=1
# # 右指针在-1后不能小于0 并且 r比r-1小    
# while r>0 and arr[r]<arr[r-1]:
#     # 右指针 从后往前移
#     r-=1

# if l==r and l!=len(arr)-1 and r!=0:
#     print("True")
# else:
#     print("False")    


# # 27. 移除元素
# nums = [3,2,2,3]
# # nums[1] = nums[3]
# val = 3
# l=0
# for r in range(len(nums)):
#     if nums[r] != val:
#         nums[l] = nums[]
#         l+=1
# print(nums)    



# 28. 找出字符串中第一个匹配项的下标
# haystack = "sadbutsaad"
# needle = "saad"
# print(haystack.find(needle)) 


# 31. 下一个排列
# def nextPermutation(nums: list[int]):
#         # 从后往前迭代
#         for i in reversed(range(len(nums) - 1)):
#             if nums[i] < nums[i + 1]:
#                 break
#             else:
#                 nums[:] = nums[::-1]
#                 return
#         j = next(j for j in reversed(range(i + 1, len(nums))) if nums[i] < nums[j])
#         nums[i], nums[j] = nums[j], nums[i]
#         nums[i + 1:] = nums[i + 1:][::-1]
#         print(nums)

# nums = [1,2,3]
# nextPermutation(nums)

# 32. 最长有效括号
# s = "()(())"
# l = 0
# r = 1
# num = 0
# while r<len(s):
#     if s[l]+s[r]=="()":
#         num+=1
#         # print(s[l]+s[r],end=" ")
#     l+=1
#     r+=1    
# print(num)     


# 33. 搜索旋转排序数组
# nums = [4,5,6,7,0,1,2]
# target = 22
# if target not in nums:
#     print(-1)
# else:
#     i=nums.index(target)
#     print(i)

# 34. 在排序数组中查找元素的第一个和最后一个位置
# nums = [5,7,7,8,8,10]
# target = 8
# n =[]
# for i,x in enumerate(nums):
#     if x==target:
#         n.append(i)
# print(n)            