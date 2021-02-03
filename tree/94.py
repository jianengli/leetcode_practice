# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        self.recursion(root)
        return self.res

    def recursion(self, root):
        if not root : return root
        if root.left:
            self.recursion(root.left)
        self.res.append(root.val)
        if root.right:
            self.recursion(root.right) 