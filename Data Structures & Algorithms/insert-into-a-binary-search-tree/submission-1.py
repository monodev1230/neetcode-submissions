# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        newNode = TreeNode(val)
        if not root:
            return newNode
        findValAndInsert(root, newNode)
        return root
        
def findValAndInsert(root, newNode):
    if not root:
        return

    if root.val > newNode.val:
        if root.left:
            findValAndInsert(root.left, newNode)
        else:
            root.left = newNode
            return
    else:
        if root.right:
            findValAndInsert(root.right, newNode)
        else:
            root.right = newNode
            return

    