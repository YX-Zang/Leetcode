class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n > 0:
            s = bin(n)[2:]
            return True if s.count('1') == 1 else False
        else:
            return False


