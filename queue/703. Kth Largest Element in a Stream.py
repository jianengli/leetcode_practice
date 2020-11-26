# 1:sorted max k numbers time:o(n*klogk)
# 2:priority queue: o(n*log2^k) 
# cus stream data, remove n from o
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.queue = nums
        self.size =len(self.queue)
        self.k=k
        heapq.heapify(self.queue)
        while self.size > k:
            heapq.heappop(self.queue)
            self.size-=1

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.size < self.k:
            heapq.heappush(self.queue,val)
            self.size+=1
        elif val > self.queue[0]:
            heapq.heapreplace(self.queue,val)
        return self.queue[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)