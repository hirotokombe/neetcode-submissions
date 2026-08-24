class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lst = []
        for i in matrix:
            lst += i
        
        L, R = 0, len(lst) - 1
        
        while L <= R: 
            m = L + (R- L) // 2
            if target < lst[m]:
                R = m - 1
            elif target > lst[m]:
                L = m + 1
            else:
                return True
        else:
            return False