# 位运算+贪心
# 链接：https://leetcode-cn.com/problems/couples-holding-hands/solution/tan-xin-suan-fa-shi-qing-lu-qian-shou-bi-eeel/ 
# time o(n^2) space o(1)
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        count = 0
        for i in range(len(row)//2):
            i = 2*i
            for j in range(i+1,len(row)):
                print(i)
                if row[i]^1 == row[i+1] : continue
                if row[i]^1 == row[j] :
                    row[i+1], row[j] = row[j], row[i+1]
                    count += 1 
                    break
        return count

