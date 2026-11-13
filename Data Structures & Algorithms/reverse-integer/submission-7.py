class Solution:
    def reverse(self, x: int) -> int:
        maxNum = (2**31) - 1
        minNum = -(2**31)
        reverseNum = 0
        while x:
            lastDigit = int(math.fmod(x, 10))
            x = int(x / 10)

            if reverseNum > maxNum // 10 or (reverseNum == maxNum // 10 and lastDigit > maxNum % 10):
                return 0
            if reverseNum < minNum // 10 or (reverseNum == minNum // 10 and lastDigit < minNum % 10):
                return 0

            reverseNum = (reverseNum * 10) + lastDigit
        
        return reverseNum