class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)

        ans = [0] * (2 * length)
        for i in range(len(nums)):
            ans[i] = ans[i + length] = nums[i]
        return ans

        