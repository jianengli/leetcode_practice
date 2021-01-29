# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.res = 0
        self.dfs(root,0)
        return self.res

    def dfs(self,root,tmp):
        if not root: return # 防止空🌲
        tmp = tmp*10 +root.val # 重点
        if root.left: 
            self.dfs(root.left,tmp)
        if root.right:
            self.dfs(root.right,tmp) 
        if not root.left and not root.right: self.res += tmp # 到叶子节点，停止计算该路径的数字
        
        # time o(n) space o(n)