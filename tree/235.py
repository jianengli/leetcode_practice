# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #非递归: Runtime: 72 ms, faster than 87.82%
        while root:
            if root.val>p.val and root.val>q.val:
                root = root.left
            elif root.val<p.val and root.val<q.val:
                root = root.right 
            else:
                return root
            
    #     #递归:Runtime: 80 ms, faster than 45.25% 
        if root.val>p.val and root.val>q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif root.val<p.val and root.val<q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        return root
    # # note: do not forget return in two 'if' statement, otherwise wrong answer appears