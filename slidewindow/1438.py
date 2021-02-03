class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        q_min = []
        q_max = []
        res = 0
        begin = 0

        for i, ele in enumerate(nums):
            while q_min and q_min[-1] > ele:
                q_min.pop()
            q_min.append(ele)

            while q_max and q_max[-1] < ele:
                q_max.pop()
            q_max.append(ele)

            while q_max[0] - q_min[0] > limit:
                if q_min[0] == nums[begin]:
                    q_min.pop(0)
                if q_max[0] == nums[begin]:
                    q_max.pop(0)
                begin += 1
            
            res = max(res, i-begin+1)
        return res