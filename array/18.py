class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        for index in range(len(nums)-3):
            if index >= 1 and nums[index] == nums[index-1]: #判重技术：当前元素与前面一致，跳过
                continue
            if nums[index]+sum(nums[-3:]) < target or sum(nums[index:index+4])>target: #优化
                continue
                
            diff = (target - nums[index]) 
            yValues = self.threeSum(nums[index+1:],diff)
            for item in yValues:
                res.append([nums[index]]+item)
        return res
    
    def threeSum(self, nums: List[int],target: int) -> List[List[int]]:
        
        res = []
        nums = sorted(nums) #Note: 要对传入的nums进行sort，而不是原来的nums
        for ia in range(len(nums)-2):
            cur, left, right = nums[ia],ia+1,len(nums)-1
            if cur+nums[left]+ nums[left+1] > target:#当前元素大于target，停止搜索
                continue
            if cur+nums[right]+ nums[right-1] < target:#当前元素小于target，停止搜索
                continue
            if ia >= 1 and nums[ia] == nums[ia-1]:#当前元素与前面一致，跳过
                continue
            
            
            while left<right:
                tsum = cur + nums[left] + nums[right]
                if tsum<target:
                    left+=1
                elif tsum>target:
                    right-=1
                else:
                    resultItem = [cur,nums[left],nums[right]]
                    if len(res) == 0 or res[-1]!=resultItem: # Note:如果 if cur not in res:会超时
                        res.append(resultItem)
                    left+=1 
                    right-=1
        return res