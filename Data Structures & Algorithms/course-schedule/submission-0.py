class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for prereq in prerequisites:
            graph[prereq[0]].append(prereq[1])
        visited = set()
        def dfs(course):
            if len(graph[course]) == 0:
                return True
            if course in visited:
                return False
            visited.add(course)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            graph[course] = []
            return True
        
        res = True
        for i in range(numCourses):
            if len(graph[i]) > 0:
                res = res and dfs(i)
        return res