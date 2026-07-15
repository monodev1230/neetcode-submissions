class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temps)
        for i, temp in enumerate(temps):
            while stack and stack[-1][0] < temp:
                prevTemp, prevInd = stack.pop()
                res[prevInd] = i - prevInd
            stack.append((temp, i))
        return res

