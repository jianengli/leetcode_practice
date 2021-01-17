class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0' : return "0"
        l1 = list(map(int,list(num1))) # 用列表储存num1的每一数位
        l2 = list(map(int,list(num2))) # 用列表储存num2的每一数位
        
        carry2 = 1 # 帮助 num2 中乘数的进位  
        res = 0
        
        # 累加 乘数的每一位与被乘数相乘得到的结果
        while l2: 
            carry1 = 1 # 帮助 num1 中被乘数的进位 
            tmp = 0 # 储存在未进位时，乘数的每一位与被乘数相乘得到的结果
            factor2 = l2.pop()
            # 将被乘数的每一位与乘数的当前位相乘，得到的结果累加，并存入tmp
            for i in range(len(l1)-1,-1,-1):
                print(i)
                tmp += l1[i]*factor2*carry1
                carry1 *= 10  # 被乘数进位
 
            res += tmp * carry2
            carry2 *= 10 # 乘数进位
        return str(res)