class Solution:
    def climbStairs(self, n: int) -> int:
        lst = [0] * (n + 1)
        lst[0], lst[1] = 1, 1
        
        for i in range(2, n + 1):
            lst[i] = lst[i - 1] + lst[i - 2]
            i += 1
        return lst[n]