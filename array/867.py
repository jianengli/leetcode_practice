# 本题的矩阵的行列数可能不等，因此不能做原地操作，需要新建数组。
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        M, N = len(matrix),len(matrix[0])
        res = [[0] * M for i in range(N)]
        for i in range(M):
            for j in range(N):
                res[j][i] = matrix[i][j]
        return res

        # import numpy as np
        # return np.transpose(matrix).tolist()