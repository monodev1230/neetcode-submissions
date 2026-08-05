class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0 or not coins:
            return 0

        q = deque()
        q.append(0)
        coinCount = 0
        seen = [False] * (amount + 1)
        while q:
            coinCount += 1
            for _ in range(len(q)):
                currAmount = q.popleft()
                for coin in coins:
                    newAmount = currAmount + coin
                    if newAmount == amount:
                        return coinCount
                    elif newAmount < amount and not seen[newAmount]:
                        q.append(newAmount)
                        seen[newAmount] = True

        return -1