class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maxarea=0
        while l<r:
            if height[r]>=height[l]:
                a=(r-l)*height[l]
                l+=1
            elif height[r]<=height[l]:
                a=(r-l)*height[r]
                r-=1
            if a>maxarea:
                maxarea=a
        return maxarea
                
