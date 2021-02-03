# 迭代
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = list()
        if not root:
            return res
         
        node = root
        stack = [node]
        while stack :
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return res

# 递归
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        self.res = []
        self.preorder(root)
        return self.res

    def preorder(self, root):
        if not root: return 
        if root:
            self.res.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)  

        # 都是 time o(n) space o(n)