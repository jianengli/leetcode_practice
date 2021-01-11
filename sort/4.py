class Solution:
    # method 1: 可以运行，但不满足题目复杂度要求
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = nums1+nums2
        res.sort()
       
        i = (len(res)-1)//2
   
         
        return (res[i]+res[i+1])/2 if len(res)%2==0 else res[i]/1
        
    # method 2