class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        visiting = set()

        for course, pre in prerequisites:
            preMap[course].append(pre)

        def dfs(course):
            if preMap[course] == []:
                return True
            if course in visiting:
                return False
            
            visiting.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False

            visiting.remove(course)
            preMap[course] = []
            
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True