# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# method 1：递归 time space o(n) o(n)
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.isBalanced = True
        self.recursion(root)
        return self.isBalanced


    def recursion(self, root):
        if not root: return 0
        left = self.recursion(root.left)
        right = self.recursion(root.right)
        if abs(left-right) > 1:
            self.isBalanced = False
        return max(left,right) + 1
             
        