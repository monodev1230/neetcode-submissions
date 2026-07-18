class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            m = (r-l)//2 + l
            if checkSplit(nums, m, k):
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res

def checkSplit(nums, maxSum, k):
    currSum = 0
    currK = 0
    for num in nums:
        currSum += num
        if currSum > maxSum:
            currK += 1
            currSum = num
    currK += 1
    if currK > k:
        return False
    return True