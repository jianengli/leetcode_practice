# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# method1 递归 没用到bst 时间复杂度高些
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.res,self.high,self.low = 0,high,low
        self.recursion(root)
        return self.res

    def recursion(self, root):
        if not root: return
        if root.val <= self.high and root.val >= self.low:
            self.res += root.val
        self.recursion(root.left)
        self.recursion(root.right)
# method2 迭代 用到bst dfs
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        res = 0 
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node:
                if node.val <= high and node.val >= low:
                    res += node.val
                    # 满足要求，左右结点都放入stack
                    stack.append(node.left)
                    stack.append(node.right)
                # 利用bst性质，nodeval<low,增加res的结点只可能在右边，所以stack中只加入右结点，从而减少time复杂度
                if node.val < low:
                    stack.append(node.right)
                # 利用bst性质，情况类似于上面
                if node.val > high:
                    stack.append(node.left)
        return res
