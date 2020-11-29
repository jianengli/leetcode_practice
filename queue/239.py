class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums: return [] # 好的编程习惯
        from collections import deque #双向队列
        deque = deque() # 储存窗口中元素的索引值，对应【左值，小值。。。】：左值需要维护，新加入元素与小值对比，确保左值总是最大值
        res = [] #储存最终结果
        for i in range(len(nums)):
            if deque and k-1<i-deque[0]:# 窗口左值索引到i步的距离大于等于k，窗口左边弹出左值
                deque.popleft()
            while deque and nums[i] > nums[deque[-1]]:# 新加入元素与小值对比，大于窗口右值，就弹出右值
                deque.pop()
            deque.append(i)# 加入新的右值的索引 
            if i >= k-1: #确保len(nums)-k+1个元素在res中
                res.append(nums[deque[0]])
        return res
    # Note: 1. in the line 10, do not reverser the order as: nums[i] > nums[deque[-1]] and deque, otherwise index out issue
    #2. 双端队列主要是用到了两点：一是在队头取当前窗口最大值，二是新进元素从队尾开始剔除小于自己的元素。对于大小为N的列表，窗口大小为K，在后面N-K次循环中，每次都会新进一个元素，剔除一个或多个元素，所以总体来看会是O(n)的时间复杂度