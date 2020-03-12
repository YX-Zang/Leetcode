class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        string = ''
        while n:
            string = chr(int((n - 1) % 26) + 65) + string
            n = (n - 1) / 26
        return string

