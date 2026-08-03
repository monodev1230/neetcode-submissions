class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        res = 0
        graph = {i: [] for i in range(n)}
        for u,v  in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node, prev):
            if node in visited:
                return
            visited.add(node)
            for neigh in graph[node]:
                dfs(neigh, node)
            
        for node in range(n):
            if node not in visited:
                dfs(node, -1)
                res += 1
        return res
            