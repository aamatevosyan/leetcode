class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxArea = 0

        while l <= r:
            minHeight = min(height[l], height[r])
            area = minHeight * (r - l)
            maxArea = max(area, maxArea)

            if minHeight == height[l]:
                l += 1
            else:
                r -= 1
        
        return maxArea
