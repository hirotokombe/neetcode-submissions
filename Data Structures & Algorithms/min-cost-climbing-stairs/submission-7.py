class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        lst = [0] * (len(cost) + 1)
       
        for i in range(2, len(cost)+ 1):
            lst[i] =  + min(cost[i-1] + lst[i - 1], cost[i-2]+lst[i - 2])
        
        return lst[len(cost)]