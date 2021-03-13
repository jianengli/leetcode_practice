class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            for j in range((len(A[0])+1)//2):
                if A[i][j]==A[i][-1-j]:
                    tmp = A[i][j]
                    A[i][-1-j]= 1-tmp 
                    A[i][j] = 1-tmp
        return A

 # 巧用规律，左右两个相同，结果反转；不同，则结果不变