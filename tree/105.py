# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.recursion(preorder,inorder)

    def recursion(self, preorder, inorder):
        if len(preorder) == 0: return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.recursion(preorder[1:mid+1],inorder[:mid]) 
        root.right = self.recursion(preorder[mid+1:],inorder[mid+1:])
        return root
        # 想问构建左右子树的时候为什么preorder以mid+1做分割？
        # 我们在 inorder 中找到 mid 为根节点的下标
# 由于中序遍历特性，mid 左侧都为左子树节点，所以左子树的节点有 mid 个
# 那么同样的，由于前序遍历的特性，preorder 第一个元素（根节点）后跟着的就是它的左子树节点，一共有 mid 个，所# 以切了 [1:mid+1] 出来