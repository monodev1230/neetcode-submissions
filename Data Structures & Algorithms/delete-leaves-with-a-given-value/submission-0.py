# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        return root if not dfs(root, target) else None

def dfs(root, target):
    if not root:
        return True
    if not root.left and not root.right and root.val == target:
        return True
    leftNode = dfs(root.left, target)
    rightNode = dfs(root.right, target)

    if leftNode:
        root.left = None
    if rightNode:
        root.right = None
    if leftNode and rightNode and root.val == target:
        return True

    return False