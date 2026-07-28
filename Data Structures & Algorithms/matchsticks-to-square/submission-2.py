class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        matchsticks.sort(reverse=True)
        squareSide = int(total / 4)
        if total % 4 != 0:
            return False
        sides = [0] * 4

        def backtrack(i, cur):
            if i == len(matchsticks):
                return True

            for side in range(4):
                sides[side] += matchsticks[i]
                if sides[side] <= squareSide and backtrack(i+1, sides[side]):
                    return True
                sides[side] -= matchsticks[i]
            return False
        res = backtrack(0, 0)
        return res