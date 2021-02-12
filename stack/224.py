https://leetcode-cn.com/problems/basic-calculator/solution/zhan-by-powcai-3/
class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        stack = []
        sign = 1 # 正负号
        i = 0
        n = len(s)
        while i < n:
            if s[i] == " ":
                i += 1
            elif s[i] == "-":
                sign = -1 # 出现负数时，可以给负数带符号
                i += 1
            elif s[i] == "+":
                sign = 1
                i += 1
            elif s[i] == "(":
                stack.append(res)
                stack.append(sign) # 储存左括号前的计算结果
                res = 0 # 便于左括号出现时，重新从0计算
                sign = 1
                i += 1
            elif s[i] == ")":
                # print(stack)
                res = res * stack.pop() + stack.pop()
                i += 1
            elif s[i].isdigit():
                tmp = int(s[i])
                i += 1
                while i < n and s[i].isdigit():
                    tmp = tmp * 10 + int(s[i])
                    i += 1
                res += tmp * sign
            print(stack,res)
        return res 