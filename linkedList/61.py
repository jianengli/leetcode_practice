# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None: return None
        if head.next == None or k == 0: return head
        move = head
        size = 0
        while move:
            move = move.next
            size += 1
        k %= size
        # print(k,size)
        if k == 0 : return head # k和链表长度一致，等于没有旋转

        # if head:[1,2,3,4,5] k=2
        start = head 
        for i in range(size-k-1):
            head = head.next
        tmp = head.next # tmp = 4
        head.next = None # 3 -> none

        dummy_node = ListNode(0)
        dummy_node.next = tmp #dum -> 4

        for j in range(k-1):
            tmp = tmp.next
        tmp.next = start # 5->1
        return dummy_node.next