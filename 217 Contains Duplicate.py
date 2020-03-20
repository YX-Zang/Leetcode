class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        long1 = len(nums)
        long2 = len(set(nums))
        return True if long1 != long2 else False
