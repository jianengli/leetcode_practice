# 双指针
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left,right = 0,0
        nums.append(float('inf'))
        max_con = 0
        for i in range(len(nums)): 
            if nums[i] == 1:
                right += 1
            elif nums[i] != 1  :
                max_con = max(max_con,right-left)
                right += 1
                left = right
        return max_con
