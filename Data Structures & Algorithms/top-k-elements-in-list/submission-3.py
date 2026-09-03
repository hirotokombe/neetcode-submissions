class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numDict = {}
        bucket = [[] for i in range(len(nums) + 1)]

        for num in nums:
            numDict[num] = numDict.get(num, 0) + 1
        
        for num, freq in numDict.items():
            bucket[freq].append(num)
        
        res = []

        for i in range(len(bucket)-1, 0, -1):
            while bucket[i]:
                val = bucket[i].pop()
                res.append(val)
                if len(res) == k:
                    return res
        
        return None
