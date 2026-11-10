class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        res = [intervals[0]]

        for r in range(1, len(intervals)):
            if res[-1][1] >= intervals[r][0]:
                res[-1][1] = max(res[-1][1], intervals[r][1])
            else:
                res.append(intervals[r])

        return res
                    
        

