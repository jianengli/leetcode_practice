class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        self.recursive(0,0,n,"")
        return self.result
        
    def recursive(self,l,r,n,result):
        if l==n and r==n:
            self.result.append(result)
            return
        if l<n:
            self.recursive(l+1,r,n,result+"(")
        if l>r and r<n:
            self.recursive(l,r+1,n,result+")")