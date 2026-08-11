class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #   [1  3]
        #.        [4   7]
        #.                 [9  11]
        #                         [13        19]
        #.          [5                14]
        # [0         5]
        # [9                                      22]

        res = []
        n = len(intervals)
        i = 0 
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        if i >= n:
            res.append(newInterval)
            return res

        newStart = min(intervals[i][0], newInterval[0])
        newEnd = newInterval[1]
        while i < n and intervals[i][0] <= newInterval[1]:
            newEnd = max(intervals[i][1], newEnd)
            i += 1
        res.append([newStart, newEnd])
        while i < n:
            res.append(intervals[i])
            i += 1
        return res
    