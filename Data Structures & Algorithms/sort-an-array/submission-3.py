class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums)
        return nums
    
    def mergeSort(self, nums):
        n = len(nums)
        if n <= 1:
            return
        mid = n//2
        leftHalf = nums[:mid]
        rightHalf = nums[mid:]
        self.mergeSort(leftHalf)
        self.mergeSort(rightHalf)

        i, j, k = 0, 0, 0
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] <= rightHalf[j]:
                nums[k] = leftHalf[i]
                i += 1
            else:
                nums[k] = rightHalf[j]
                j += 1
            k += 1
        while i < len(leftHalf):
            nums[k] = leftHalf[i]
            i += 1
            k += 1
        while j < len(rightHalf):
            nums[k] = rightHalf[j]
            j += 1
            k += 1
