class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left = 0
        size = len(A)
        zero_count,max_len = 0,0
        for i in range(size): 
            if A[i] == 0:
                zero_count += 1
            if zero_count > K: 
                while A[left] != 0:
                    left += 1
                left += 1
                zero_count -= 1 
            max_len = max(max_len, i-left+1) # 注意不能属于上一个if内部，否则会出现全1的最长连续数组被忽视的情况
        return max_len