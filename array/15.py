class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) < 3:
            return []
        res = []
        nums.sort()
        for ia in range(len(nums)-2):
            if nums[ia] > 0:#当前元素大于0，停止搜索
                break
            if ia >= 1 and nums[ia] == nums[ia-1]:#当前元素与前面一致，跳过
                continue
            # method 2: double pointer timeO(n^2) spaceO(1) almost 1 times faster than method 1
            cur, left, right = nums[ia],ia+1,len(nums)-1
            while left<right:
                tsum = cur + nums[left] + nums[right]
                if tsum<0:
                    left+=1
                elif tsum>0:
                    right-=1
                else:
                    resultItem = [cur,nums[left],nums[right]]
                    if len(res) == 0 or res[-1]!=resultItem: # Note:如果 if cur not in res:会超时
                        res.append(resultItem)
                    left+=1 
                    right-=1
        return res
            
#             method 1: hash map timeO(n^2) spaceO(n) use hashmap
#             target = - nums[ia]
#             hashmap = {}
#             for index in range(ia+1, len(nums)):
#                 diff = (target - nums[index]) 
#                 if diff in hashmap.keys():
#                     cur = [nums[ia], diff,nums[index]]
                    
#                     if len(res) == 0 or res[-1]!=cur: # Note:如果 if cur not in res:会超时
#                         res.append([nums[ia], diff,nums[index]])
#                 else:
#                     hashmap[nums[index]] = index
        
        
        # return res