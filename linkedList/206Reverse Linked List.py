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
    