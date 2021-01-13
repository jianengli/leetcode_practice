class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # method 1 time：O(n^2) 
        # 横向纵向遍历对比所有子字符串
        # 考虑2种特殊情况
        if not strs: return ""
        if len(strs) == 1: return strs[0]
        res = ""
        tmp = ""
         
        for index in range(len(strs[0])):
            res = tmp
            # print(tmp,'res',res)
            tmp = strs[0][:index+1]
            for pos in range(len(strs)):
                # print(tmp,strs[pos][:index+1])
                if tmp != strs[pos][:index+1]:
                     
                    return res
        res = tmp            
                
        return res
    
    # Runtime: 32 ms, faster than 78.98% of Python3 online submissions for Longest Common Prefix.
    # Memory Usage: 14.3 MB, less than 52.77% of Python3 online submissions for Longest Common Prefix.