class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = defaultdict(list)
        
        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1

        res = []
        def dfs(course):
            indegree[course] -= 1
            res.append(course)

            for neighbor in adj[course]:
                indegree[neighbor] -= 1
                
                if indegree[neighbor] == 0:
                    dfs(neighbor)

          

        for course in range(numCourses):
            if indegree[course] == 0:
                dfs(course)
        
        return res if len(res) == numCourses else []