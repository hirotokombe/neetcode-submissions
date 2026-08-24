class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        length = len(nums)
        for i in range(len(nums)):
            while nums[i] == val:
                nums = self.removeOneElement(nums, length, i)
                length -= 1
        k = length
        return k
        
    def removeOneElement(self, nums: List[int], length: int, index: int) -> List[int]:
        for i in range(index, length - 1):
            nums[i] = nums[i+1]
        nums[length - 1] = None
        return nums