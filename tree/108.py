# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getBSTree(self, nums):
        if not nums:
            return None
        mid = len(nums)//2
        root = TreeNode(nums[mid])

        left = nums[:mid]
        right = nums[mid+1:]

        root.left = self.getBSTree(left)
        root.right = self.getBSTree(right)

        return root

if __name__ == "__main__":
    solution = Solution()
    nums = [-10,-3,0,5,9]
    sorted_lists = solution.getBSTree(nums)
    print(sorted_lists)
