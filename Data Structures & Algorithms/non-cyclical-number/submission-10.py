class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.squareDigits(n)
        
        while slow != fast:
            slow = self.squareDigits(slow)
            fast = self.squareDigits(fast)
            fast = self.squareDigits(fast)
        
        return fast == 1



    def squareDigits(self, n):
        total = 0

        while n:
            digit = n % 10
            total += digit ** 2
            n = n // 10
        return total