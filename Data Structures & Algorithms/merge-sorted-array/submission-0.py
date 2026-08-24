class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for j in nums2: 
            index = nums1.index(0)
            nums1[index] = j


        for i in range(1, len(nums1)):
            j = i - 1
            while j >= 0 and nums1[j+1] < nums1[j]:
                temp = nums1[j+1]
                nums1[j+1] = nums1[j]
                nums1[j] = temp
                j -= 1