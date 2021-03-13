# 要求 不用额外空间 - 》nums 充当哈希表 -〉原地修改
# 如何修改？ 利用这一范围之外的数字，来表达「是否存在」的含义
# https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/solution/zhao-dao-suo-you-shu-zu-zhong-xiao-shi-d-mabl/
 
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        for ele in nums:
            print(ele)
            
            nums[(ele-1)%n] += n # 关键操作-取模，可能之前的 +n 改动到了后面ele，从而数组溢出，取模保证不溢出
        for i in range(n):
            if nums[i] <= n :
                res.append(i+1)
        return res

