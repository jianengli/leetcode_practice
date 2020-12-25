class Solution:
    def totalNQueens(self, n: int) -> int:
        self.result =[]
        self.DFS([],[],[],n)
        return len(self.result)
        
    def DFS(self, queens, yx_dif,yx_sum,n):
        depth = y = len(queens)
        if depth == n:
            self.result.append(queens)
            return
        for x in range(n):
            if x not in queens and y-x not in yx_dif and y+x not in yx_sum: 
                self.DFS(queens+[x],yx_dif+[y-x],yx_sum+[y+x],n)