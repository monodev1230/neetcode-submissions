class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q = deque()
        direCount = 0
        radCount = 0
        for s in senate:
            if s == 'D':
                direCount += 1
            else:
                radCount += 1
            q.append(s)
        
        diffDire = 0
        diffRad = 0
        
        while radCount != 0 and direCount != 0:
            currSenate = q.popleft()
            
            if currSenate == "R":
                if diffRad > 0:
                    diffRad -= 1
                    radCount -= 1
                    continue
                diffDire += 1
            else:
                if diffDire > 0:
                    diffDire -= 1
                    direCount -= 1
                    continue
                diffRad += 1
            q.append(currSenate)
        return "Radiant" if direCount == 0 else "Dire"

