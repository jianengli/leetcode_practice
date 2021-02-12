class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        self.word1,self.word2 = word1, word2
        return self.recursion(0,0)
        
    import functools
    @functools.lru_cache(None)    
    def recursion(self, i,j):
        if len(self.word1)==i or len(self.word2)==j:
            return len(self.word1)-i + len(self.word2)-j
        if self.word1[i] == self.word2[j]:
            return self.recursion(i+1,j+1)
        else:
            inserted = self.recursion(i,j+1)
            deleted = self.recursion(i+1,j)
            swaped = self.recursion(i+1,j+1)
            return min(inserted,deleted,swaped)+1