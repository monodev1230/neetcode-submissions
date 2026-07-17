class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return binarySearch(nums, 0, len(nums) - 1, target)
    
def binarySearch(nums, start, end, target):
    if start > end:
        return -1
    mid = (end - start)//2 + start
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return binarySearch(nums, start, mid - 1, target)
    return binarySearch(nums, mid + 1, end, target)