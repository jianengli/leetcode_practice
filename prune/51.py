class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.result = []
        self.DFS([],[],[],n)
        return [["."*i+"Q"+"."*(n-1-i) for i in sol] for sol in self.result]
    
    def DFS(self, queen_list,xy_diff,xy_sum,n):
        y = len(queen_list)
        if y == n:
            self.result.append(queen_list)
            return  
        for x in range(n):
            if x not in queen_list and y-x not in xy_diff and y+x not in xy_sum:
                self.DFS(queen_list+[x],xy_diff+[y-x],xy_sum+[y+x],n)
            
        