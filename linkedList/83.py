# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return head
        dummy_node = ListNode(0)
        dummy_node.next = head 
        while head.next:
            if head.next.val == head.val:
                tmp = head.next.next
                head.next = tmp
            else:
                head = head.next
        return dummy_node.next
            