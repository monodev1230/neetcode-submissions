from heapq import *
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t: t[1])
        currLoad = []
        currPass = 0
        for pCnt, start, end in trips:
            while currLoad and currLoad[0][0] <= start:
                currPass -= heappop(currLoad)[1]
            currPass += pCnt
            if currPass > capacity:
                return False
            heappush(currLoad, (end, pCnt))
        return True