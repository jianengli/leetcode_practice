# https://leetcode-cn.com/problems/sort-an-array/solution/python-shi-xian-de-shi-da-jing-dian-pai-xu-suan-fa/
# 归并 
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        mid = len(nums)//2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left,right)

    def merge(self, left,right):
        res = []
        i,j = 0,0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1      
        res += left[i:] # 不是 append
        res += right[j:]
        return res

# 冒泡 o(n^2) 超时
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for z in range(len(nums)):
            for i in range(len(nums)-1-z):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
        return nums

# 插入排序 o(n^2)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for z in range(1,len(nums)): 
            while z>0 and nums[z]<nums[z-1]:
                nums[z],nums[z-1] = nums[z-1],nums[z] 
                z -= 1
        return nums