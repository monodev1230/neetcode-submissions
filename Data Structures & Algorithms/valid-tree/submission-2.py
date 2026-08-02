class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        graph = {i: [] for i in range(n)}
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        def dfs(node, prev):
            if node in visited:
                return False

            visited.add(node)
            for neigh in graph[node]:
                if neigh == prev:
                    continue
                if not dfs(neigh, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n
                    