# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyNode = ListNode(0) #三个指针一般新建node，二个pre=none;引入了第三个指针，记录每一步反转后第二个node地址，原因：下一步更新node链接时，会涉及到第一步的node
        pre = dummyNode
        pre.next = head
        
        while pre.next and pre.next.next:
            cur = pre.next # cur->1
            future = cur.next
            
            # pre.next,future.next,cur.next = future,cur,future.next
            
            cur.next = future.next# first, 1->3 （这步放后面会超时）
            future.next = cur
            pre.next = future #不指向2，表头都无
            
            pre = cur #前驱节点的更新
        return dummyNode.next
        