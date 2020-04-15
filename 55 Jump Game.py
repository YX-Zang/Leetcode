class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach = 0
        for index, v in enumerate(nums):
            if index > reach:
                return False
            reach = max(reach, index + v)
        else:
            return True
