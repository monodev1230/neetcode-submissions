class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = searchRow(matrix, target)
        if row >= len(matrix):
            return False

        left, right = 0, len(matrix[row]) - 1
        while left <= right:
            mid = (right - left)//2 + left
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False

        
def searchRow(matrix, target):
    top, bot = 0, len(matrix) - 1
    while top <= bot:
        mid = (bot - top) // 2 + top
        if matrix[mid][0] > target:
            bot = mid - 1
        elif matrix[mid][-1] < target:
            top = mid + 1
        else:
            return mid
        return top
