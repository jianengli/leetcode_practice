# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
            #method 1 :bfs
    
        if not root: return 0
        
        # result = []
        openlist = collections.deque()
        closedlist = set() #对图得加这个
        cost = 0
         
        openlist.append(root)

        while openlist:
            depth_size = len(openlist)
            current_depth_list = []  
            for _ in range(depth_size):
                node = openlist.popleft()
                if node not in closedlist:
                    current_depth_list.append(node.val)
                    if node.left: openlist.append(node.left)
                    if node.right: openlist.append(node.right)
            # result.append(current_depth_list)
            cost = cost + 1
        
        return cost
    
    #method2:iterative deepen search