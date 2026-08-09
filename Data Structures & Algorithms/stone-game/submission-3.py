class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        alice = 0
        aliceChoices = []
        bobChoices = []
        bob = 0
        isAlice = True
        left, right = 0, n - 1
        for _ in range(n):
            leftValue = piles[left] - piles[left+1] if left + 1 < n else piles[left]
            rightValue = piles[right] - piles[right-1] if right - 1 >= 0 else piles[right]
            if leftValue > rightValue:  
                if isAlice:
                    alice += piles[left]
                    aliceChoices.append(piles[left])
                else:
                    bob += piles[left]
                    bobChoices.append(piles[left])
                left += 1
            else:
                if isAlice:
                    alice += piles[right]
                    aliceChoices.append(piles[right])
                else:
                    bob += piles[right]
                    bobChoices.append(piles[right])
                right -= 1
            isAlice = not isAlice
        return True
