from itertools import combinations
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        list1 = [i for i in range(1, n+1)]
        return [i for i in combinations(list1, k)]