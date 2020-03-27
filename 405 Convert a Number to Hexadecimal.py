class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num >= 0:
            return hex(num)[2:]
        else:
            return hex(2 ** 32 + num)[2:]
