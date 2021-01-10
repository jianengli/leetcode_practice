class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        range3,range9,set9 = range(3),range(9),set(str(x) for x in range(1,10)) #set9 每个空格的可能性为1-9
        def DFS():
            for y,row in enumerate(board):
                for x,char in enumerate(row):
                    if char != '.':
                        continue
                    for choosen in set9 - {row[k] for k in range9} - {board[k][x] for k in range9} - {board[y//3*3+m][x//3*3+n] for m in range3 for n in range3}: # 对于一个位置，初始化的集合取值 减去 其他限制位置已经出现过的数值，最终得到候选
                        board[y][x] = choosen
                        if DFS(): return True # 直到找到结果
                        board[y][x] = '.'
                        
                    return False
            return True
        DFS()
    link：https://b23.tv/YBrYBy
    # {row[k] for k in range9} 考虑第y列的限制L其他位置存在的数值构成的数组
    # {board[k][x] for k in range9} 考虑第x列的限制：其他位置存在的数值构成的数组
    # {board[y//3*3+m][x//3*3+n] for m in range3 for n in range3} 考虑当前宫格的限制：宫格中其他位置存在的数值构成的数组
