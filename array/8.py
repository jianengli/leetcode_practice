class Solution:
    # method 1: 考虑多种情况，要细心
    def myAtoi(self, s: str) -> int:
        lower_bound, upper_bound = 2 ** 31 * -1, 2 ** 31 - 1 
        string = s.strip() 
        if not string or string == '0':
            return 0
        
        isNegative = False
        isPositive = False
        if string[0] == "-":
            string = string[1:] 
            isNegative = True 
        elif string[0] == "+":
            string = string[1:] 
            isPositive = True 
            
        l=list(map(str,list(string)))
        
        if not l or not l[0].isdigit() :
            return 0
        
        for i in range(len(l)):
            if not l[i].isdigit() :
                l=l[:i]
                break 
                
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
        elif isPositive:
            res += '+'
            for i in range(len(l)):
                res += str(l[i])
        else:
            for i in range(len(l)):
                res += str(l[i])
        res = int(res)
        
        if res <= - 2 ** 31:
            return lower_bound
        elif res >= 2 ** 31:
            return upper_bound
        else:
            return res
# Runtime: 36 ms, faster than 56.83% of Python3 online submissions for String to Integer (atoi).
# Memory Usage: 14.1 MB, less than 78.02% of Python3 online submissions for String to Integer (atoi).             