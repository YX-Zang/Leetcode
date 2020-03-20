class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for index, v in enumerate(nums):
            if index != v:
                return index
        else:
            return nums[-1] + 1
