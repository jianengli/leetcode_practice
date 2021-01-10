# -*- coding:utf-8 -*-
#method1
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        hashmap={}
        for each in numbers:
            hashmap[each]=hashmap.get(each,0)+1
        counter = 0
        for element in numbers:
            if hashmap[element]>1:
                duplication[0] = element
                counter+=1
                break
        return counter>=1       


#method2: 85.7%通过 ；解法二：高赞回答里的“高级方法” 前排说一下，这种方法并不能够输出“第一个重复的数字”，举例：[3,2,1,1,3]，第一个重复的数字是3，但是输出是1
# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        index = 0
        while index < len(numbers):
            if numbers[index] == index:
                index += 1
            elif numbers[index] == numbers[numbers[index]]:
                duplication[0] = numbers[index]
                return True
            else:
                index_2 = numbers[index]
                numbers[index],numbers[index_2] = numbers[index_2],numbers[index]
        return False