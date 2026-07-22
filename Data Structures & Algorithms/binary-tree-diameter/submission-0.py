# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.diameter

    def dfs(self, root):
        if not root:
            return 0
        dLeft = self.dfs(root.left)
        dRight = self.dfs(root.right)
        res = max(dLeft, dRight)
        self.diameter = max(self.diameter, dLeft + dRight, res)
        return res + 1