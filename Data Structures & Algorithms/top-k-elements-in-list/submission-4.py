class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []
        lst = [[] for i in range(len(nums) + 1)]

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for i, val in freq.items():
            lst[val].append(i)
        
        for i in range(len(nums), -1, -1):
            while lst[i]:
                res.append(lst[i].pop())
                if len(res) == k:
                    return res

        return None
