class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)

        ans = [0] * (2 * length)
        i = 0
        j = 0
        while i < len(nums) and j < len(ans):
            ans[j] = nums[i]
            if i == len(nums) - 1:
                i = -1
            i += 1
            j += 1
        return ans

        