"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        nodeMap = {}
        def deepcopy(n):
            if not n:
                return
            nodeMap[n] = Node(n.val)
            if n.neighbors:
                newNeighs = []
                for neigh in n.neighbors:
                    if neigh not in nodeMap:
                        deepcopy(neigh)
                    newNeighs.append(nodeMap[neigh])
                nodeMap[n].neighbors = newNeighs
            return nodeMap[n]
        deepcopy(node)
        return nodeMap[node]
