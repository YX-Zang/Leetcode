class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.guessIn(1, n)

    def guessIn(self, left, right):
        mid = (left + right) // 2
        if guess(mid) == 0:
            return mid
        else:
            return self.guessIn(left, mid - 1) if guess(mid) == -1 else self.guessIn(mid + 1, right)