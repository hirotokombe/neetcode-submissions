class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxValue = 0
        for i in range(len(arr) - 1):
            for v in range(i+1, len(arr)):
                if arr[v] > maxValue:
                    maxValue = arr[v]
            arr[i] = maxValue
            maxValue = 0
        arr[-1] = -1
        return arr
        

        