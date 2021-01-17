class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: return []

        self.res = []
        self.length = len(nums)
        self.recursion([],nums)
        return self.res
        
    '''
    choosen列表储存一种新的排列的元素
    candidates列表存储待选的元素
    '''
    def recursion(self,choosen,candidates):
        if len(choosen) == self.length: # 当 choosen 长度达到要求，加入返回列表res中
            self.res.append(choosen)  
            return
        for i in range(len(candidates)): # 遍历 candidates列表 每个待选，放入到choosen，递归直到产生一种新的排序
            tmp1 = choosen.copy() 
            tmp1.append(candidates[i])

            tmp2 = candidates.copy() 
            del (tmp2[i])

            self.recursion(tmp1,tmp2) 
