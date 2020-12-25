class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        range3,range9,set9 = range(3),range(9),set(str(x) for x in range(1,10))
        def DFS():
            for y,row in enumerate(board):
                for x,char in enumerate(row):
                    if char != '.':
                        continue
                    for choosen in set9 - {row[k] for k in range9} - {board[k][x] for k in range9} - {board[y//3*3+m][x//3*3+n] for m in range3 for n in range3}:
                        board[y][x] = choosen
                        if DFS(): return True
                        board[y][x] = '.'
                        
                    return False
            return True
        DFS()
                        