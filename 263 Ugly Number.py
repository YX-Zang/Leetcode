class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num >= 2 ** 31 or num < -2 ** 31 - 1:
            return False
        while num:
            if num % 2 == 0:
                num /= 2
            elif num % 3 == 0:
                num /= 3
            elif num % 5 == 0:
                num /= 5
            else:
                if num == 1:
                    return True
                else:
                    return False