# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced, height = dfs(root)
        return isBalanced

def dfs(root):
    if not root:
        return (True, 0)
    
    isLeftBalanced, dLeft = dfs(root.left)
    isRightBalanced, dRight = dfs(root.right)
    height = max(dRight, dLeft)
    return (abs(dLeft - dRight) <= 1 and isLeftBalanced and isRightBalanced, height + 1)