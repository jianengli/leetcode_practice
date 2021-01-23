# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while slow and fast and fast.next: # 注意不要忘记检查fast.next的存在
            slow, fast = slow.next, fast.next.next 
            if slow is fast:
                return True
            
        return False

    # 1. do not forget to check whether fast.next exists