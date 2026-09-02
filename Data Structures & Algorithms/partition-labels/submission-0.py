class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freqMap = {}
        for i, ch in enumerate(s):
            if ch in freqMap:
                cnt, start, end = freqMap[ch]
                freqMap[ch] = (cnt + 1, start, i)
            else:
                freqMap[ch] = (1, i, i)
        i = 0
        res = []
        while i < len(s):
            cur = s[i]
            cnt, start, end = freqMap[cur]
            if cnt == 1:
                res.append(1)
                i += 1
                continue
            curEnd = end
            j = i + 1
            while j < curEnd:
                _, _, newEnd = freqMap[s[j]]
                curEnd = max(curEnd, newEnd)
                j += 1

            res.append(j - i + 1)
            i = j + 1
        return res

                

