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
        cur = dummy_node
        while cur.next and cur.next.next:
            tmp = cur.next
            if tmp.val == tmp.next.val:
                while tmp.next and tmp.val == tmp.next.val:
                    tmp = tmp.next
                cur.next = tmp.next
            else:
                cur = cur.next
        return dummy_node.next