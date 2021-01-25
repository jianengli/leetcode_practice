# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    # method 1
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        res = [] 
        move = head 
        while move :
            res.append(move.val)
            move = move.next
        if res == res[::-1]: return True
        return False