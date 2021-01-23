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