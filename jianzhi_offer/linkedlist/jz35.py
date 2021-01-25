"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return head
        hashmap = dict()
        # 3. 复制各节点，并建立 “原节点 -> 新节点” 的 Map 映射
        cur = head
        while cur:
            hashmap[cur] = Node(cur.val)
            cur = cur.next
        # 4. 构建新节点的 next 和 random 指向
        cur = head
        while cur:
            hashmap[cur].next = hashmap.get(cur.next) # 新链表中cur位置上node的next指向 新链表中cur.next位置上node
            hashmap[cur].random = hashmap.get(cur.random) # 新节点random指向随机的新节点
            cur = cur.next
        # 5. 返回新链表的头节点
        return hashmap[head]