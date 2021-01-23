class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.length = len(nums)
        if self.length == 0: return []
        self.res = []
        self.res.append([])
        self.recursion(nums)
        return self.res 

    def recursion(self, candidates):
        if len(candidates) == 0: 
            return 
        tmp = self.res.copy() # 复制除去candidates外元素形成的子集 

        # 添加candidates中第一个元素到 tmp 中每一个子集
        for i in range(len(tmp)): 
            self.res.append(tmp[i]+[candidates[0]])  
        del candidates[0] # 用完这个元素，从 candidates中移除
        self.recursion(candidates)
 
