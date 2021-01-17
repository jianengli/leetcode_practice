class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        left, right = 0, len(nums)-1
        while  left <= right:
            mid = (left + right)//2
            if target == nums[mid]:
                return mid
            if nums[mid] < nums[left]: # 中间值在右边区域
                if nums[mid] <= target and target <= nums[right]: # target 在mid 和 right 中间
                    left = mid + 1
                else:
                    right =  mid - 1
            elif nums[mid] >= nums[left]: # 中间值在左边区域
                if nums[left] <= target and target <= nums[mid]: # target 在 left 和 mid 中间
                    right =  mid - 1
                else:
                    left = mid + 1 
        return -1
