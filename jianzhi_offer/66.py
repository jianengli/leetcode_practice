# -*- coding:utf-8 -*-
import collections
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        self.row, self.col = rows,cols
        self.dict=set()
        self.search(threshold,0,0)
        return len(self.dict) # 求满足题意要求（if not self.judge(threshold, i, j) or (i,j) in self.dict）时，字典长度就为所求
    
    def judge(self,threshold,i,j):
        return sum(map(int,list(str(i))))+sum(map(int,list(str(j))))<=threshold
    
    def search(self,threshold,i,j):
        if not self.judge(threshold, i, j) or (i,j) in self.dict: return
        self.dict.add((i,j))
        if i<self.row-1:
            self.search(threshold, i+1, j)
        if j<self.col-1:
            self.search(threshold, i, j+1)

          # 要注意去重:(i,j) in self.dict 如果不加这一句，时间复杂度不会满足。  
        
        
        
        
#         def BFS():
#             if rows == 0 and cols ==0: return 0
#             count=0
#             openlist = collections.deque()
#             closedlist = set()
#             self.row,self.col = 0,0
            
#             openlist.append((self.row,self.col ))
#             arr[self.row][self.col] = 1
            
#             while [[0 in arr[i][j] for i in range(cols)] for j in range(rows)]:
#                 node = openlist.popleft()
                
#                 if self.row+1<=rows and self.row+1>=0 and self.col<=cols and self.col>=0 and arr[self.row+1][self.col]==0:
#                     count+=1
#                     openlist.append((self.row+1,self.col ))
#                     arr[self.row][self.col] = 1
                
            
            
            
#             return count
        
#         arr = [[0 for i in range(cols)] for j in range(rows)]
#         for j in range(rows):
#             for i in range(cols):
#                 if not self.checkValid(threshold, j, i):
#                     arr[j][i] = -1
#         print(arr)
#         self.BFS()
        
        
                    
#     def checkValid(self,threshold, row, col):
#         sum = 0
#         while row:
#             sum += row%10
#             row /= 10
#         while col:
#             sum += col%10
#             col /= 10
#         if sum >= threshold:
#             return False
#         return True