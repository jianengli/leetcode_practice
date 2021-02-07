# question 14- I
# method 1 math time O(1)
class Solution:
    def cuttingRope(self, n: int) -> int: 
        if n == 0 or n == 1: return n
        if n == 2 or n == 3: return n - 1 
        a, b = n//3, n%3
        print(a,b) 
        if b == 1:
            return int(math.pow(3,a-1))*4
        elif b == 2:
            return int(math.pow(3,a)*b) # 注意不是pow(a,3)
        elif b == 0:
            return int(math.pow(3,a))

# question 14- II
# 循环取余 time O(n)
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n == 0 or n == 1: return n
        if n == 2 or n == 3: return n - 1 
        a, b, x, p  = n//3, n%3, 3, 1000000007
        res = 1 # 不要忘记初始化
        for i in range(a-1):
            res = (res * x ) % p
        if b == 1:
            return int(res)*4%p
        elif b == 2:
            return int(res*6)%p  # 注意不是pow(a,3)
        elif b == 0:
            return (int(res*3))%p
# method 2 快速幂求余 time O(log2^n)