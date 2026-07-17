class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0 
        stack = []
        for i, height in enumerate(heights):
            leftExtInd = i
            while stack and stack[-1][0] >= height:
                prevHeight, prevInd = stack.pop()
                maxArea = max(maxArea, prevHeight * (i-prevInd))
                leftExtInd = prevInd
            stack.append((height, leftExtInd))

        while stack:
            currHeight, currInd = stack.pop()
            maxArea = max(maxArea, currHeight * (len(heights) - currInd))

        return maxArea
            