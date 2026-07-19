from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start = 0
        res = []
        q = deque()
        for end in range(len(nums)):
            while q and nums[q[-1]] < nums[end]:
                q.pop()
            q.append(end)
            if start > q[0]:
                q.popleft()
            if end + 1 >= k:
                res.append(nums[q[0]])
                start += 1
        return res