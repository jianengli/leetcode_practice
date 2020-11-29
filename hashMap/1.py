class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for index in range(len(nums)):
            diff = (target - nums[index]) 
            if diff in hashmap.keys():
                return [hashmap[diff],index]
            else:
                hashmap[nums[index]] = index