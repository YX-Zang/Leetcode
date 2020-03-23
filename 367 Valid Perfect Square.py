class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        sqr = '%d' % num ** 0.5
        return True if int(sqr)**2 == num else False

