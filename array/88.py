class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer,pointer1, pointer2 = 0,0,0
        nums1_copy = nums1[:m].copy()
        # 防止 list 的 index 溢出
        nums1_copy.append(float('inf'))
        nums2.append(float('inf'))

        # 推进双指针，填充 nums1
        while pointer < m+n :
            if nums1_copy[pointer1] == float('inf'): 
                nums1[pointer] = nums2[pointer2]
                pointer2 += 1
            elif nums2[pointer2] == float('inf'): 
                nums1[pointer] = nums1_copy[pointer1]
                pointer1 += 1
            elif nums1_copy[pointer1] >= nums2[pointer2]:
                nums1[pointer] = nums2[pointer2]
                pointer2 += 1
            elif nums1_copy[pointer1] < nums2[pointer2]:
                nums1[pointer] = nums1_copy[pointer1]
                pointer1 += 1
            pointer += 1

# 2.6
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2: return nums1
        i,j = 0,0
        res = []
        # nums1 = nums1[:m] 
        while i <= len(nums1[:m] )-1 and j <= len(nums2)-1: 
            if nums1[:m] [i] <= nums2[j]:
                res.append(nums1[:m][i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        
        res += (nums1[:m][i:])
        res += (nums2[j:]) 
        for i in range((m+n)):  
            nums1[i] = res[i]
         
        return nums1 

# method 2 逆向双指针 空间减到o(1)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0: 
            nums1[:] =nums2[:]
            return nums1
        i,j,p = m-1, n-1, len(nums1)-1
        while j>=0:
            if i<0:
                nums1[p] = nums2[j]
                j -= 1
                p -= 1
            else:
                if nums1[i]>=nums2[j]:
                    nums1[p] = nums1[i]
                    i -= 1
                    p -= 1
                else:
                    nums1[p] = nums2[j]
                    j -= 1
                    p -= 1 
        return nums1
 
# 参考思路 https://leetcode-cn.com/problems/merge-sorted-array/solution/he-bing-liang-ge-you-xu-shu-zu-by-leetcode/ 