# 归并排序 待优化 
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
 
        global counter  
        counter = 0 
        # write code here
        l,r=0,len(nums)-1
        self.MergeSort(l,r,nums) 
        return counter 
    
    def MergeSort(self,l,r,nums): 
        global counter
        if r-l<1: 
            return  
        mid = (l+r)//2
        self.MergeSort(l,mid,nums)
        self.MergeSort(mid+1,r,nums)
        self.Merge(l,mid,r,nums) 
         
        
    def Merge(self,l,mid,r,nums):
        global counter     
        
        L = nums[l:mid+1]
        R = nums[mid+1:r+1] 
        L.append(float('inf') )
        R.append(float('inf') )
        # print(L,R)
        i,j,k  = 0,0,l
        # print(l,mid,r)
        while k<=r:
            # print(L[i],R[j])
            if L[i] == float('inf'):
                nums[k] = R[j]
                j += 1
            elif R[j] == float('inf'):
                nums[k] = L[i]
                i += 1
            elif L[i]>R[j]: 
                nums[k] = R[j]
                j += 1
                counter += len(L)-1-i
            else:
                nums[k] = L[i]
                i += 1  
            k += 1 
# 执行用时：
# 3152 ms
# , 在所有 Python3 提交中击败了
# 5.02%
# 的用户
# 内存消耗：
# 19.2 MB
# , 在所有 Python3 提交中击败了
# 46.95%
# 的用户