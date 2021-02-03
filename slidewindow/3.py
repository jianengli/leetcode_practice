class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        size = len(s)
        max_length = 0
        cur_length = 0
        left = 0
        lookup = set() 

        for i in range(size):
            cur_length += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_length -= 1

            lookup.add(s[i]) 
            if cur_length > max_length:
                max_length = cur_length
        return max_length

