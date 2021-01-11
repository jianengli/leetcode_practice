# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0) # 返回链表的头节点
        move = res # 为res每个节点赋值的中间节点
        tmp = 0 # 进位值
        while l1 != None or l2 != None:
            if l1 == None:
                l2,l1 = l1,l2 # 交换位置，避免再次讨论一个链表走完后的情况（我们只讨论链表l2走完的情况，如下面）
            if l2 != None:
                tmp, l1.val = divmod(l1.val+l2.val+tmp,10)
                move.next = l1
                l2,l1,move = l2.next,l1.next,move.next
            else:
                tmp, l1.val = divmod(l1.val+tmp,10)
                move.next = l1
                l1,move = l1.next,move.next
        if tmp == 1: # l1 链表 在最后一位时，进位值为1时，应当使得res链表指向1
            move.next = ListNode(tmp)
        return res.next
    
# https://b23.tv/yrl66u