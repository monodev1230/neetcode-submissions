# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return dfs(root)
        
def dfs(root):
    if not root:
        return 0
    depthLeft = dfs(root.left)
    depthRight = dfs(root.right)
    return max(depthLeft, depthRight) + 1