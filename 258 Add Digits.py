class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            n1 = num // 10
            n2 = num % 10
            num = n1+n2
        else:
            return num
