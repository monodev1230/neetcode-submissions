class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        end = float("-inf")
        removed = 0

        for start, finish in intervals:
            if start >= end:
                end = finish
            else:
                removed += 1

        return removed