"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        prevEnd = float('-inf')
        intervals.sort(key = lambda i: i.start)
        for interval in intervals:
            if prevEnd > interval.start:
                return False
            prevEnd = interval.end
        return True