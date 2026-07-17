class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0 
        stack = []
        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][0] > height:
                prevHeight, prevInd = stack.pop()
                maxArea = max(maxArea, prevHeight * (i-prevInd))
                start = prevInd
            stack.append((height, start))

        for currHeight, currInd in stack:
            maxArea = max(maxArea, currHeight * (len(heights) - currInd))

        return maxArea
            