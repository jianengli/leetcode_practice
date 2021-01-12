class Solution:
    def reverse(self, x: int) -> int:
        # 思路：先判断是否为负数，分2种情况反转数值部分；然后将反转后数值变为数组，将多余的0删去（如果有的话）；最后根据正负情况，将数组合并成字符串，再变为int型
        if x == 0:
            return x
        string = str(x)
        isNegative = False
        if string[0] == '-':
            string = string[1:][::-1]
            isNegative = True
        else:
            string = string[::-1]
        l=list(map(int,list(string)))
        while l:
            if l[0] == 0:
                l.remove(l[0])
            else:
                break
        res = '' 
        
        if isNegative:
            res += '-'
            for i in range(len(l)):
                res += str(l[i])
        else:
            for i in range(len(l)):
                res += str(l[i])
        res = int(res)
        return res if res >= - 2 ** 31  and res <= 2 ** 31 - 1 else 0
        # Runtime: 36 ms, faster than 37.93% of Python3 online submissions for Reverse Integer.
# Memory Usage: 14.2 MB, less than 41.86% of Python3 online submissions for Reverse Integer.

# Runtime: 32 ms, faster than 68.23% of Python3 online submissions for Reverse Integer.
# Memory Usage: 14.3 MB, less than 41.86% of Python3 online submissions for Reverse Integer.