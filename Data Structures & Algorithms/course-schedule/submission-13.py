class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1

        res = []

        def dfs(course):
            indegree[course] -= 1   # Mark this course as already processed
            res.append(course)

            for neighbor in adj[course]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    dfs(neighbor)

        for course in range(numCourses):
            if indegree[course] == 0:
                dfs(course)

        return len(res) == numCourses