# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        inorder = sorted(preorder)
        
        return self.helper(preorder,inorder)

    def helper(self,preorder,inorder):
        if  not (preorder):return None
        root = TreeNode(preorder[0])
        rootIndex = inorder.index(root.val)

        root.left = self.helper(preorder[1:rootIndex+1],inorder[0:rootIndex+1])
        root.right = self.helper(preorder[rootIndex+1:],inorder[rootIndex+1:])

        return root

        # https://leetcode-cn.com/problems/construct-binary-search-tree-from-preorder-traversal/solution/tu-jie-gou-zao-er-cha-shu-jian-dan-yi-do-gq4y/