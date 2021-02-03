class Solution:
    def reverseWords(self, s: str) -> str:
        list_s = s.split() 
        # list_s = s.split(" ")
        # list_s = [x.strip() for x in list_s if x.strip() != ''] 
        l,r = 0, len(list_s)-1
        while l<r:
            list_s[l],list_s[r] = list_s[r], list_s[l]
            l += 1
            r -= 1
        return " ".join(list_s)