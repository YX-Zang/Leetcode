# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 0
        r = n
        while True:
            if isBadVersion((l + r) // 2):
                r = (l + r) // 2
            elif not isBadVersion((l + r) // 2):
                l = (l + r) // 2
            if abs(r - l) <= 1:
                if isBadVersion(r) or isBadVersion(l):
                    if isBadVersion(r):
                        return r
                    else:
                        return l


def isBadVersion(version):
    if version == 4:
        return True
    else:
        return False
