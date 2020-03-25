class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n1 = list(set(nums))
        n1.sort()
        if len(n1) < 3:
            return n1[-1]
        else:
            return n1[-3]
