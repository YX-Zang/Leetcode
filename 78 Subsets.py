from itertools import combinations
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        list1 = []
        for x in range(len(nums)+1):
            for i in combinations(nums, x):
                list1.append(list(i))
        return list1