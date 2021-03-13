class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        n,m = len(nums),len(nums[0])
        if n*m != r*c: return nums
        # one_dimension = [0 for _ in range(r*c)]
        # for i in range(n):
        #     for j in range(m):
        #         one_dimension[i*m+j] = nums[i][j] 
        # res = []
        # for z in range(r):
        #     t = []
        #     for h in range(c): 
        #         print(one_dimension[z*c+h])
        #         t.append(one_dimension[z*c+h])
        #     res.append(t)
        res = [[0] * c for _ in range(r)]
        for x in range(m * n):
            res[x // c][x % c] = nums[x // m][x % m]
 
        return res

# time o(n*n) space o(1)