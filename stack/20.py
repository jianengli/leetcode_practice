class Solution:
    def isValid(self, s: str) -> bool:
        # 时间复杂度O(n),空间复杂度O(n)。
        stack = []
        pattentheses_map = {')':'(',']':'[','}':'{'}
        for ele in s:
            if ele in pattentheses_map:
                if not stack or pattentheses_map[ele]!=stack.pop():
                    return False 
            else:
                stack.append(ele) # put left pattenthesis into the stack
        return not stack # stack无元素返回true，有元素返回false

        # Runtime: 24 ms, faster than 95.81% of Python3 online submissions for Valid Parentheses.
        # Memory Usage: 14.5 MB, less than 7.68% of Python3 online submissions for Valid Parentheses.
