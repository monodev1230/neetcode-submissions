class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #flip
        n = len(matrix)
        for r in range(n//2):
            for c in range(n):
                matrix[n-1-r][c], matrix[r][c] = matrix[r][c], matrix[n-1-r][c]

        #transpose
        for r in range(n):
            for c in range(r + 1, n):
                matrix[c][r], matrix[r][c] = matrix[r][c], matrix[c][r]
        
