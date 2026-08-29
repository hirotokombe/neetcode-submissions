class Solution:
    def countBits(self, n: int) -> List[int]:
        lst = [0] * (n + 1)
        for i in range(n+1):
            lst[i] = lst[i >> 1] + (i & 1)
        return lst