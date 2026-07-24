from heapq import *
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = []
        freqMap = Counter(tasks)
        for k, v in freqMap.items():
            heappush(maxHeap, -v)
        time = 0 # 2

        q = deque()

        while maxHeap or q:
            time += 1
            if not maxHeap:
                time = q[0][1]
            else:
                count = 1 + heappop(maxHeap)
                if count:
                    q.append((count, time + n))
            if q and q[0][1] == time:
                heappush(maxHeap, q.popleft()[0])
        return time 

                
            
