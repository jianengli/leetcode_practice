# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_value = -float('inf')
        self.recursion(root)
        return self.max_value

    def recursion(self,root):
        if not root: return 0
        left = max(0,self.recursion(root.left)) # 左边子树返回值，不考虑负数
        right = max(0,self.recursion(root.right)) # 右边子树返回值，不考虑负数
        sum = left + right + root.val
        self.max_value = max(self.max_value, sum) # 维护最大路径和

        return root.val + max(left,right)