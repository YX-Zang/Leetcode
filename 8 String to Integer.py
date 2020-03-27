import re


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        res = re.findall('(^[\+\-]?\d+)', str)
        num = int(res[0]) if res else 0
        if num >= 2 ** 31:
            return 2 ** 31 - 1
        elif num <= -2 ** 31:
            return -2 ** 31
        else:
            return num
