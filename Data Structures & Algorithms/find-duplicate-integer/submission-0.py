class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        x = 0
        while fast < len(nums) + 1:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                x = slow
                break
        slow = 0
        while slow != x:
            slow = nums[slow]
            x = nums[x]
        return slow