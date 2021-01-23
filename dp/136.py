class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tmp = 0
        for i in range(len(nums)): 
            tmp ^= nums[i]
        return tmp