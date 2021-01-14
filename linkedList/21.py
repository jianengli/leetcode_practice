# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # time O(m+n) space O(1)
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None:
            return l1
        dummy_node = ListNode(10086)
        move = dummy_node
        
        while l1 != None or l2 != None: # if l1 == none: <==> if l1: 
            if not l2 or (l1 and l1.val <= l2.val) :
                tmp = l1
                l1 = l1.next
                move.next = tmp
            elif not l1 or (l2 and l1.val > l2.val) :
                tmp = l2
                l2 = l2.next
                move.next = tmp
            move = move.next
        
        return dummy_node.next

        # Runtime: 36 ms, faster than 75.02% of Python3 online submissions for Merge Two Sorted Lists.
        # Memory Usage: 14.2 MB, less than 82.78% of Python3 online submissions for Merge Two Sorted Lists.

        # Runtime: 20 ms, faster than 99.97% of Python3 online submissions for Merge Two Sorted Lists.
        # Memory Usage: 14.4 MB, less than 29.94% of Python3 online submissions for Merge Two Sorted Lists.