class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        cycle = set()
        graph = {i: [] for i in range(n)}
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        def dfs(node, prev):
            if len(graph[node]) == 1 and graph[node][0] == prev:
                visited.add(node)
                return True
            if node in cycle:
                return False
            cycle.add(node)
            visited.add(node)
            for neigh in graph[node]:
                if neigh != prev and not dfs(neigh, node):
                    return False
            cycle.remove(node)
            return True
        
        if not dfs(0, -1):
            return False
        print(visited)
        if len(visited) < n:
            return False
        return True
                    