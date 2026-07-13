class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        itemsToRemove = []
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                itemsToRemove.append(i)
        print(itemsToRemove)
        for i in range(len(itemsToRemove)-1,-1,-1):
            del nums[itemsToRemove[i]]
            print(nums)
        
        return len(nums)