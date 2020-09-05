"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
"""
class Solution(object):
    #time:o(1)*n=o(n),space:o(n)
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        pattentheses_map={')':'(',']':'[','}':'{'}
        for p in s:
            print(not stack)
            if p not in pattentheses_map:
                # put left pattenthesis into the stack
                stack.append(p)
                
            elif not stack or pattentheses_map[p]!=stack.pop():
                return False
        return not stack# it means there is no element in stack,  and return true