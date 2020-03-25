class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = int(num1)
        num2 = int(num2)
        if num2 is 0:
            return str(num1)
        return self.addStrings(num1 ^ num2, (num1 & num2) << 1)

