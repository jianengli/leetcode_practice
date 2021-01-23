# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2: return l1
        move = dummy_node = ListNode(0) # move 指向 dummynode
        carry = 0 # 进位值
        
        while l1 or l2 :
            if not l1 and l2:
                tmp = l2
                l2 = l1
                l1 = tmp 
            if not l2 and l1:
                carry, l1.val = divmod(l1.val + carry,10)   
                move.next = l1
                move = move.next
                l1 = l1.next
            elif l1 and l2:
                carry, l1.val = divmod(l1.val + l2.val + carry, 10)
                move.next = l1
                move = move.next
                l1,l2 = l1.next,l2.next
            
            # # 不要忘记最后一位可能再进一位
            if carry == 1:
                move.next = ListNode(carry) 

        return dummy_node.next
