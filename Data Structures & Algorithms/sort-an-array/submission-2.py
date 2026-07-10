class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        merge_sort(nums)
        return nums
    
    # def quickSort(self, nums, left, right):
    #     if left < right:
    #         partitionPos = self.partition(nums, left, right)
    #         self.quickSort(nums, left, partitionPos - 1)
    #         self.quickSort(nums, partitionPos + 1, right)
    #     return nums
    
    # def partition(self, nums, left, right):
    #     pivot = nums[right]
    #     i = left - 1
    #     for j in range(left, right):
    #         if nums[j] < pivot:
    #             i += 1
    #             nums[j], nums[i] = nums[i], nums[j]
    #     nums[i + 1], nums[right] = nums[right], nums[i + 1]
    #     return i + 1

def merge_sort(arr):
    # Base case: a list of 0 or 1 elements is already sorted
    if len(arr) <= 1:
        return arr

    # Step 1: Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Step 2: Conquer (Recursively sort both halves)
    merge_sort(left_half)
    merge_sort(right_half)

    # Step 3: Combine (Merge the sorted halves back into the original array)
    i = j = k = 0

    # Compare elements from both halves and place the smaller one into arr
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # Pick up any remaining elements from left_half
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    # Pick up any remaining elements from right_half
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1