class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            x = nums.pop(0)
            if x not in nums:
                return x
            else:
                nums.remove(x)


