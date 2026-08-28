class Solution:
    def isHappy(self, n: int) -> bool:
        digitSum = 0
        seenInteger = {}
        while digitSum != 1:
            digitSum = 0
            for integer_char in str(n):
                integer = int(integer_char)
                digitSum += (integer ** 2)
            
            if digitSum in seenInteger:
                return False
            
            seenInteger[digitSum] = n
            n = digitSum
        
        return True


        