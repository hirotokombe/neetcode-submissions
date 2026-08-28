class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        newLst = []
        n = self.listToInteger(digits) + 1
        for i in str(n):
            newLst.append(int(i))
        
        return newLst


    def listToInteger(self, lst: List[int]) -> int:
        power = len(lst)
        total = 0
        for i in range(len(lst)):
            total += lst[i] * (10 ** (power-1))
            power -= 1        
        return total