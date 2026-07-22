# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        qStr = dfs(q, "")
        pStr = dfs(p, "")
        return qStr==pStr
def dfs(node, res):
    if not node:
        return 'E'
    resL = dfs(node.left, res)
    resR = dfs(node.right, res)
    return resL + 'L' + str(node.val) + resR + 'R'