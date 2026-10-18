class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = defaultdict(list)

        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1

        res = []

        def dfs(course):
            # So courses that had indegree == 0 will get -1 so it doesnt get processed again
            indegree[course] -= 1  
            res.append(course)

            for neighbor in adj[course]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    dfs(neighbor)

        for course in range(numCourses):
            if indegree[course] == 0:
                dfs(course)

        return len(res) == numCourses