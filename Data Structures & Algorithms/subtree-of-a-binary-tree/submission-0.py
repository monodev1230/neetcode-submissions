# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot or not root:
            return False
        return self.dfs(root, subRoot)
        
    def dfs(self, root, subRoot):
        if not root:
            return
        isSame = False
        if root.val == subRoot.val:
            isSame = self.isSameTree(root, subRoot)
        return self.dfs(root.left, subRoot) or self.dfs(root.right, subRoot) or isSame


    def isSameTree(self, root1, root2):
        if not (root1 and root2):
            return root1 == root2
        return root1.val == root2.val and self.isSameTree(root1.left, root2.left) and self.isSameTree(root1.right, root2.right)
    