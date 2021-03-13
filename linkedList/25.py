# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummyNode = ListNode(0)
        dummyNode.next = head
        end = pre = dummyNode
        
        def swap( pre,end,k):
            after = end.next
            move = pre.next
            pre.next = end 
            temp = move.next
            end =move
        
            for i in range(k-1):
                tnext = temp.next
                temp.next = move
                move = temp
                temp = tnext
            end.next=after

            return end
    
        while True:
            try:
                for _ in range(k):
                    end = end.next
                
                pre = end = swap(pre,end,k)
            except:
                print(222)
                break
                    
        return dummyNode.next
    
#         for i in range(k):
#                 end = end.next
                
#         while pre == end and end == swap(pre,end,k):
#             for i in range(k):
#                 end = end.next

#     def swap(self, pre,end,k):
#         after = end.next
#         move = pre.next
#         pre.next = end 
#         temp = move.next
#         end =move
        
#         for i in range(k-1):
#             tnext = temp.next
#             temp.next = move
#             move = temp
#             temp = tnext
#         end.next=after

#         return end

# 2.18
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head: return None
        dummy_node = ListNode(0)
        move = dummy_node.next = head
        count = 0
        while move:
            count += 1
            move = move.next 
        
        pre,cur = dummy_node,head 
        stack = []
        for i in range(count//k):
            
            for j in range(k): 
                n = ListNode(cur.val)
                stack.append(n)
                cur = cur.next  
            while stack:
                tmp = stack.pop()
                pre.next = tmp
                pre = tmp 
        while cur:
            pre.next = cur
            pre = cur   
            cur = cur.next
        return dummy_node.next