# 不用重开数组，递归的空间利用率高
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.prev = None
        return self.helper(root)
    
    def helper(self,root):
        if root is None:
            return True
        if not self.helper(root.left):
            return False
        if self.prev and self.prev.val >= root.val:
            return False
        self.prev = root
        return self.helper(root.right)
        #Runtime: 48 ms, faster than 31.19% of Python3 online submissions for Validate Binary Search Tree.

# TO DO: has bug : TypeError: isValidBST() missing 2 required positional arguments: 'min' and 'max'   
# class Solution:
#     def isValidBST(self, root: TreeNode, min , max  ) -> bool:
#         if root is None:
#             return True
#         if (min is not None) and (root.val<=min): 
#             return False
#         if (max is not None ) and (root.val>=max): 
#             return False
    
#         return isValidBST(root.right, min, root.val) and isValidBST(root.right, root.val,max)