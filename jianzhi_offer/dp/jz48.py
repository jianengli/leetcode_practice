class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # dp = [0 for _ in range(len(s))]
        t, max_value = 0, 0 
        hashmap = {}
        i = -1
        for j in range(len(s)):
            print(j)
            if s[j] in hashmap.keys():
                i = hashmap[s[j]]
            # if dp[j-1] >= j-i:
            #     dp[j] = j-i
            # else:
            #     dp[j] = dp[j-1]+1
            if t >= j-i:
                t = j-i
            else:
                t = t + 1
            max_value = max(t,max_value)
            hashmap[s[j]] = j
        return max_value
        # if dp:
        #     return max(dp) 
        # else:
        #     return 0