class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maxWater = -1
        while left < right:
            currWater = (right - left) * min(heights[left], heights[right])
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            maxWater = max(maxWater, currWater)
        return maxWater