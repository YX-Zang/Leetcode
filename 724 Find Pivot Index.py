class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        for i in range(0, len(nums)):
            left = nums[:i]
            right = nums[i + 1:]
            if sum(left) == sum(right):
                return i
        return -1