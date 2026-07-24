# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = [float('-inf')]
        dfs(root, maxSum)
        return maxSum[0]

def dfs(root, maxSum):
    if not root:
        return 0 
    leftPath = dfs(root.left, maxSum)
    rightPath = dfs(root.right, maxSum)


    maxSum[0] = max(maxSum[0], leftPath + rightPath + root.val)
    return max(0, root.val, root.val + leftPath, root.val + rightPath)