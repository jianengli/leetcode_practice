# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool: 
        return self.recursion(root, targetSum)
        

    def recursion(self, root, diff):
        if not root:
            return False
        if not root.left and not root.right:
            return diff == root.val
        return self.recursion(root.left,diff-root.val) or self.recursion(root.right,diff-root.val)
        # return or是左右子树只要有一条路径满足条件就可以返回true 但是and是左右子树路径必须所有都满足条件 与题意不符合