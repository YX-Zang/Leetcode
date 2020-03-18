class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1 = [i for i in s]
        s2 = [i for i in t]
        s1.sort()
        s2.sort()
        return True if s1 == s2 else False
