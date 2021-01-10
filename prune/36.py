class Solution:# 验证当前输入的数独是否有效即可
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        visited = {} # 存储每一行每一列，每一个3*3宫格中出现过的数字；如果在判断中，见到这个数字，返回false（表示其无效） 
        for x in range(9):
            for y in range(9): 
                d = board[x][y]
                if d=='.':
                    continue
                z = (x//3)*3 + (y//3)# 判断当前位置是在哪一个3*3宫格中 【0-8】
                if (z,d) in visited or (0,x,d) in visited or (1,y,d) in visited:
                    return False
                # 把当前数字存储到相对应的行列以及3*3宫格中
                visited[(z,d)] = 1
                visited[(0,x,d)] = 1
                visited[(1,y,d)] = 1
        return True