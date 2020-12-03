# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (root is None): # 到达空节点，返回为空
            return None
        if (p is root) or (q is root):
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left is None: #左子树遍历到空节点，也没发现p or q
            return right
        elif right is None:#右子树遍历到空节点，也没发现p or q
            return left
        else:
            return root
        #Note：递归精髓：在函数未写好前，也可以用。因为这个函数功能与返回值，我是知道的。根据这个函数功能与返回值，用上它后，好处是可以将底层的递归坍缩，比如left = self.lowestCommonAncestor(root.left,p,q)：只考虑一层左子树，从而变成只有1个左节点的二叉树，便于思考