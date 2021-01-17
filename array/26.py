class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer = 0
        tmp = float('inf')
        while pointer < len(nums):
            if nums[pointer] != tmp:
                tmp = nums[pointer]
                pointer += 1
            else:
                del nums[pointer]
        return len(nums)