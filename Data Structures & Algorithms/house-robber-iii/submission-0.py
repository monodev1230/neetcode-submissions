# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return (0, 0)
            withLeft, withoutLeft = dfs(root.left)
            withRight, withoutRight = dfs(root.right)
            withRoot = root.val + withoutLeft + withoutRight
            withoutRoot = max(withLeft, withoutLeft) + max(withRight, withoutRight)

            return (withRoot, withoutRoot)
        withRoot, withoutRoot = dfs(root)
        print(withRoot, withoutRoot)
        return max(withRoot, withoutRoot)
