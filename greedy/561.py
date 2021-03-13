# 也是作为一种贪心的选择吧，对于包含nums最大值的(ai,bi)对，min(ai,bi)一定不是这个nums的最大值，我们贪心地将nums的第二大值放在这个(ai,bi)对里，这样这个min(ai,bi)就能取最大，除去这两个值后，剩下的n-1对也是如此，这样可以保证这n对都取最大
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])
