class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node, prev):
            if len(graph[node]) == 1 and graph[node][0] == prev:
                return 1
            maxChildHeight = -1
            for neigh in graph[node]:
                if neigh == prev:
                    continue
                maxChildHeight = max(maxChildHeight, dfs(neigh, node))
            return maxChildHeight + 1
        heightTrees = {i: [] for i in range(1, n + 1)}
        for i in range(n):
            heightTrees[dfs(i, -1)].append(i)
        for i in range(1, n+1):
            if len(heightTrees[i]) > 0:
                return heightTrees[i]
        return []