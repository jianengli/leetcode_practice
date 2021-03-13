# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        stack,res = [],[]
        while head:
            stack.append(head.val)
            head = head.next
        while stack:
            res.append(stack.pop())
        return res
            