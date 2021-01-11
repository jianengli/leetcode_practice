class Solution:
    def longestPalindrome(self, s: str) -> str:
        string = ''
        for i in range(len(s)):
            start = max(0,i-len(string)-1) # 确保候选1长度比string长2
            tmp = s[start:i+1]
            if tmp == tmp[::-1]: # 判断候选1是否是回文
                string = tmp
            else:
                tmp = tmp[1:] # 候选1去掉首节点，变为候选2
                if tmp == tmp[::-1]: # 判断候选2是否是回文
                    string = tmp
        return string