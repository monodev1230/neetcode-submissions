class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        visited = set()
        graph = {i: [] for i in range(numCourses)}
        for prereq in prerequisites:
            graph[prereq[0]].append(prereq[1])

        def dfs(crs):
            if crs in visited:
                return False
            if len(graph[crs]) == 0:
                if crs not in res:
                    res.append(crs)
                return True
            visited.add(crs)
            for prereq in graph[crs]:
                if not dfs(prereq):
                    return False
            visited.remove(crs)
            graph[crs] = []
            res.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res
            