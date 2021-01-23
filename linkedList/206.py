# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # method 1
    # def reverseList(self, head: ListNode) -> ListNode:
    #     l=self.getList(head)
    #     l.reverse()
    #     dummy = p = ListNode(0)
    #     for val in l :
    #         p.next = ListNode(val)
    #         p = p.next
    #     return dummy.next
        
    # def getList(self, head):
    #     l=[]
    #     while head:
    #         l.append(head.val)
    #         head=head.next
    #     return l
        
    #     l = []
    #     while head:
    #         l.append(head.val)
    #         head = head.next
    #     return l
    
    #method 2
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return None
        pre = None
        cur = head
        while cur:
            
            cur.next, pre, cur = pre, cur, cur.next
        return pre

# 1.19再写，不如前面精简
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         if head == None: return head
#         dummy_node = ListNode(0)
#         move = head
#         while move.next != None:
#             move = move.next 
#         move.next = dummy_node

#         pre, cur = None, head
#         while cur != None:
#             tmp = cur.next
#             cur.next = pre
#             pre = cur
#             cur = tmp
        
#         return dummy_node.next