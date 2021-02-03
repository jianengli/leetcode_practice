class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = set(nums)
        cur_len,max_len = 0,0
        for ele in hashmap:
            if ele - 1 not in hashmap:
                cur_len = 1
                while ele + 1 in hashmap:
                    cur_len += 1
                    ele += 1
                max_len = max(cur_len,max_len)
        return max_len

        # time O（n） space O（n）

        # for ele in hashmap:
        #     cur_len = 0
        #     if ele-1 in hashmap:
        #         cur_len += 1
        #         while ele in hashmap:
        #             cur_len += 1
        #             ele += 1
        #         max_len = max(cur_len,max_len)
        #     else:
        #         cur_len = 1
        #         max_len = max(cur_len,max_len)
        # return max_len
        # 反思： 上面的时间复杂度高，因为在 while ele in hashmap中，又对ele进行了判断，ele 必然在hashmap中


             
# class Solution:
#     def longestConsecutive(self, nums):
#         longest_streak = 0
#         num_set = set(nums)

#         for num in num_set:
#             if num - 1 not in num_set:
#                 current_num = num
#                 current_streak = 1

#                 while current_num + 1 in num_set:
#                     current_num += 1
#                     current_streak += 1

#                 longest_streak = max(longest_streak, current_streak)

#         return longest_streak 