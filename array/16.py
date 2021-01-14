class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # double pointer timeO(n^2) spaceO(1)
        # 思路：在problem15上改进边可以
        
        min_sum = 99999
        res = 0
        nums.sort()
        
        for ia in range(len(nums)-2): # 注意确保a,b,c一定有3个元素
 
            if ia >= 1 and nums[ia] == nums[ia-1]:#当前元素与前面一致，跳过
                continue
             
            cur, left, right = nums[ia],ia+1,len(nums)-1

            while left<right:
                tsum = cur + nums[left] + nums[right]
                # 比 problem15 增加的代码
                dif = abs(tsum - target)
                tmp = min(min_sum, dif)
                if tmp != min_sum: # 出现更小的差值时
                    min_sum = tmp # 记录目前出现的最小差值
                    res = tsum # 记录当前的3 sum
                    
                if tsum < target:
                    left+=1
                elif tsum > target:
                    right-=1
                else:
                    return target

        return res

        # Runtime: 112 ms, faster than 86.41% of Python3 online submissions for 3Sum Closest.
        # Memory Usage: 14.3 MB, less than 41.31% of Python3 online submissions for 3Sum Closest.