class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        if not intervals:
            return res
        intervals.sort()
        currStart = intervals[0][0]
        currEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] > currEnd:
                res.append([currStart, currEnd])
                currStart = interval[0]
                currEnd = interval[1]
            else:
                currStart = min(currStart, interval[0])
                currEnd = max(currEnd, interval[1])
        res.append([currStart, currEnd])
        return res