class Solution:
    # method 1
    def majorityElement(self, nums: List[int]) -> int:
        return self.help(0,len(nums)-1,nums)
        
        
    def help(self,low,high,nums):
        if low == high:
            return nums[low]
        mid = (high-low)//2 + low
        left = self.help(low,mid,nums)
        right = self.help(mid+1,high,nums)
        if left == right:
            left
        left_count = sum(1 for i in range(low,high+1) if nums[i]==left)
        right_count = sum(1 for i in range(low,high+1) if nums[i]==right)
        return left if left_count > right_count else right

class Solution:
    # method 2 
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]