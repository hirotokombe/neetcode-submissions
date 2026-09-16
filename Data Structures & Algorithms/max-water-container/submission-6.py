class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxVal = 0

        while l < r:
            minHeight = min(heights[l], heights[r])
            area = minHeight * (r - l)
            maxVal = max(maxVal, area)
            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1
        
        return maxVal