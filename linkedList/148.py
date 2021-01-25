# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head: return head
        sublength = 1
        list_length = 0
        cur = head
        while cur:
            cur = cur.next
            list_length += 1
        
        move = dummy_node = ListNode(10086)
        dummy_node.next = head
        # while sublength < list_length:
        # move = dummy_node

        node_size = 0
        cur = head
        while cur:
            cur = cur.next
            node_size += 1

        cur = head
        merge_time, left = divmod(node_size,2)
        print(merge_time, left)
        for i in range(merge_time):
            head1 = cur
            print(cur )
            for _ in range(sublength):
                # print(cur )
                cur = cur.next
            head2 = cur
            for _ in range(sublength):
                cur = cur.next
            merged = self.merge(head1, head2)
            move.next = merged
        if left == 1:
            move.next = cur
            
            # sublength *= 2

        return dummy_node.next

    def merge(self, l1:ListNode, l2:ListNode):
        move = dummy_node = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                move.next = l1
                l1 = l1.next
            else:
                move.next = l2
                l2 = l2.next
            move = move.next
        if l1:
            move.next = l1
        elif l2:
            move.next = l2
        # while not l1 or not l2:
        #     if not l1 and l2 :
        #         move.next = l2
        #         l2 = l2.next
        #     elif not l2 and l1:
        #         move.next = l1
        #         l1 = l1.next
        #     move = move.next

        return dummy_node.next
    
