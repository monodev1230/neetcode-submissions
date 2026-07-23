# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return dfs(root, -1000)

def dfs(root, maxOnPath):
    if not root:
        return 0 
    res = 0 
    if maxOnPath <= root.val:
        res += 1
    res += dfs(root.left, max(maxOnPath, root.val))
    res += dfs(root.right, max(maxOnPath, root.val))

    return res