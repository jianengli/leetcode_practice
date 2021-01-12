class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 : return False
        res,tmp = 0,x
        # 反转 x
        while tmp:
            res = res*10 + tmp%10 # 将 tmp 反转
            tmp //= 10 # 进位
        return res == x # 判断是否回文
        