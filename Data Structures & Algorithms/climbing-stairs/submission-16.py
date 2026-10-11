class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        one, two = 1, 2   # stair 1, stair 2

        for i in range(2, n):
            tmp = two
            two = one + two
            one = tmp

        return two