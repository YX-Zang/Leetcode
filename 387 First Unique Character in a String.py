class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        ls1 = list(s)
        for index, v in enumerate(ls1):
            if s.count(v) == 1:
                return index
        else:
            return -1
