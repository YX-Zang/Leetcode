class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        rank = []
        rank.extend(nums)
        rank.sort(reverse=True)
        for index, v in enumerate(nums):
            index2 = rank.index(v) + 1
            if index2 == 1:
                nums[index] = 'Gold Medal'
            elif index2 == 2:
                nums[index] = 'Silver Medal'
            elif index2 == 3:
                nums[index] = 'Bronze Medal'
            else:
                nums[index] = str(index2)

        return nums