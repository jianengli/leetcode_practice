class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        num = 1 
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        x,y = 0,0 # x,y 记录当前坐标

        # 填充首行元素
        for y in range(n):
            matrix[0][y] = num
            num += 1  
        
        # 用 tmp 推进顺时针矩形的收缩
        tmp = n

        while num <= n*n:
            # 顺时针矩形外圈右边 
            for _ in range((tmp)-1):
                x += 1 # 坐标进入新的顺时针矩形
                matrix[x][y] = num
                num += 1  

            # 顺时针矩形外圈下边     
            for _ in range((tmp)-1):
                y -= 1
                matrix[x][y] = num
                num += 1 

            # 顺时针矩形外圈左边     
            for _ in range((tmp)-2):
                x -= 1
                matrix[x][y] = num
                num += 1

            # 顺时针矩形外圈上边    
            for _ in range((tmp)-2):
                y += 1
                matrix[x][y] = num
                num += 1 
            
            tmp -= 2 # 走完一个外圈，顺时针矩形的收缩 2 个单位
        
        return matrix

