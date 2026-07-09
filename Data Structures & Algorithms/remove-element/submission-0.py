class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count, currInd = 0, 0
        for i, num in enumerate(nums):
            if num == val:
                count += 1
            else:
                if currInd < i:
                    nums[currInd] = num
                currInd += 1
        return len(nums) - count