class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        nums.sort()
        n = 1
        while nums:
            if n not in nums:
                return n
            else:
                n += 1
