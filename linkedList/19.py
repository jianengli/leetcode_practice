# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        move = dummy_node = ListNode(0)
        dummy_node.next = head
        size = 0
        while move.next:
            move = move.next
            size += 1 
        move = dummy_node 
        for i in range(size-n): 
            move = move.next 
        tmp = move.next.next
        move.next = tmp 
        return dummy_node.next

