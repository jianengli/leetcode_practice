class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # method 1: O(nlogn)
        # return sorted(s) == sorted(t)
        
        # method 2: O(n) in python, we use hashMap
        dict1,dict2 = {},{}
        for item in s:
            dict1[item] = dict1.get(item,0) + 1
        for item in t:
            dict2[item] = dict2.get(item,0) + 1
        return dict1==dict2
            