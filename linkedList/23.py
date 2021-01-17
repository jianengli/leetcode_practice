# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists)==0  :
            return None
        res = lists
        
        while len(res) > 1:
            merge_time = len(res)//2 
            if len(res)%2 == 1: merge_time += 1
            tmp = []
            for i in range(merge_time):
                
                if (i+1)*2 <= len(res):
                    # print(i,res[i*2],res[i*2+1])
                    tmp.append(self.merge(res[i*2],res[i*2+1]))
                else:
                    print("true")
                    # print(i,res[-1])
                    tmp.append(res[-1])
            # print(tmp)
            res = tmp
        return res[0]
        

    def merge(self, l1: List[ListNode],l2: List[ListNode] ):
        move = dummy_node = ListNode(10086)
        while l1 or l2:
             
            if not l1:
                move.next = l2
                l2 = l2.next    
            elif not l2:
                move.next = l1
                l1 = l1.next         
            elif l1.val <= l2.val and l1 and l2:
                move.next = l1
                l1 = l1.next
            elif l1.val > l2.val and l1 and l2:
                move.next = l2
                l2 = l2.next
            move = move.next
        # print(dummy_node.next)
        return dummy_node.next

            
