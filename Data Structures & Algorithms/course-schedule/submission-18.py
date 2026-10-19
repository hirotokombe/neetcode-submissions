class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1
        
        res = []
        def dfs(course):     
            res.append(course)
            indegree[course] -= 1
            for neighbor in adj[course]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    dfs(neighbor)
                
        for course in range(numCourses):
            if indegree[course] == 0:
                dfs(course)
        
        return True if len(res) == numCourses else False