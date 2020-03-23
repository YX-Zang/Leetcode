class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        long1 = len(nums)
        nums2 = [x for x in nums if x != 0]
        long2 = len(nums2)
        nums[0:] = nums2 + [0] * (long1 - long2)