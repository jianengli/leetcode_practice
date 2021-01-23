class DoubleLinkedList:
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None # DoubleLinkedList(0)

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        # 使用伪头部和伪尾部节点 
        self.head, self.tail = DoubleLinkedList(), DoubleLinkedList()
        self.head.next, self.tail.pre = self.tail, self.head
        

    def get(self, key: int) -> int: 
        # 如果 key 存在，先通过哈希表定位，再移到头部
        if key in self.cache.keys():
            node = self.cache[key] # 字典的value值是 DoubleLinkedList 对象
            self.move2Head(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None: 
        if key in self.cache.keys():
            node = self.cache[key]
            node.val = value # 变更其数据值
            self.move2Head(node)
        else: # 如果 key 不存在，创建一个新的节点
            new_node = DoubleLinkedList(key,value)
            self.cache[key] = new_node 
            self.add2Head(new_node) # 不要忘记添加 node至链表头部

            if len(self.cache.keys()) > self.capacity: 
                removed_node = self.removeFromTail()
                # 不要忘记 删除哈希表中对应项
                del self.cache[removed_node.key] 

    def move2Head(self, node):
        self.removeNode(node)
        self.add2Head(node)
    
    def removeNode(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def add2Head(self, node):
        # 安排好self.head, self.head 和 node 的 next 和 pre
        tmp = self.head.next
        node.pre = self.head
        node.next = tmp
        tmp.pre = node
        self.head.next = node

    def removeFromTail(self):
        removed_node = self.tail.pre
        self.removeNode(removed_node)
        return removed_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)