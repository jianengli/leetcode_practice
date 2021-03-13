class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        hashmap, m, n = dict(), len(matrix), len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if hashmap.setdefault(i-j,matrix[i][j])!= matrix[i][j]:
                    return False
        return True