class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 双指针法 time:o(n), 左右两个指针向中间逼近。边长在一直减小，要获取更大的面积，只有改动短板长度，最短的板子才可能会变大。所以在每一次遍历时，将短板向中间变换。
        l,r = 0,len(height)-1
        max_water = 0
        while(l<r):
            water = min(height[l],height[r])*(r-l)
            max_water = max(water,max_water)
            if height[l] <= height[r]:
                l+=1
            else:
                r-=1
        return max_water
        
        # method 1 o(n^2) 超时
        # max_water = 0
        # for i in range(len(height)):
        #     for j in range(i+1,len(height)):
        #         water = min(height[i],height[j])*(j-i)
        #         max_water = max(water,max_water)
        # return max_water