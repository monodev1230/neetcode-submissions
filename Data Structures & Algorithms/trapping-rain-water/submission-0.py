class Solution:
    def trap(self, height: List[int]) -> int:
        leftWall = [0] * len(height)
        rightWall = [0] * len(height)
        res = 0

        leftHighest = 0
        for i in range(len(height)):
            leftWall[i] = leftHighest
            leftHighest = max(height[i], leftHighest)
        #[0,0,2,2,3,3,3,3,3,3]
        rightHighest = 0
        for i in range(len(height) - 1, -1, -1):
            rightWall[i] = rightHighest
            rightHighest = max(height[i], rightHighest)
        #[3,3,3,3,3,3,3,2,1,0]
        #[0,0,2,0,2,3,2,0,0,0]
        for i in range(len(height)):
            res += max(0, min(rightWall[i], leftWall[i]) - height[i])
        return res