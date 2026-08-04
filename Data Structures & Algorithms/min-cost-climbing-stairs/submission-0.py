class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        costs = [0] * n
        costs[-1] = cost[-1]
        costs[-2] = cost[-2]
        for i in range(n-3, -1, -1):
            costs[i] = cost[i] + min(costs[i+1], costs[i+2])

        return min(costs[0], costs[1])
            