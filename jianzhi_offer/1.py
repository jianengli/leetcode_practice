# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        j = 0
        i = len(array[0])-1
        
        while i>=0 and j<=len(array)-1:
            try:
                if target > array[j][i]:
                    j = j+1
                elif target < array[j][i]:
                    i = i-1
                elif target == array[j][i]:
                    return True
            except:
                break
        return False

# 理解：https://www.bilibili.com/video/BV1Tt411F7YD?from=search&seid=16715786949984645008