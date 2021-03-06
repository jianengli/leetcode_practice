class Solution:
    #method 1 :bfs
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        
        result = []
        openlist = collections.deque()
        closedlist = set() #对图得加这个
         
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
            result.append(current_depth_list)
        
        return result
    
    #method2:iterative deepen search