class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curr, pick):
            if len(curr) == len(nums):
                res.append(curr.copy())
            for i in range(len(nums)):
                if not pick[i]:
                    curr.append(nums[i])
                    pick[i] = True
                    backtrack(curr, pick)
                    curr.pop()
                    pick[i] = False
                    
        backtrack([], [False] * len(nums))
        return res