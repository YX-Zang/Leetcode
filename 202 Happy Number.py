class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ls1 = []
        while n != 1:
            res = self.add_sum(n)
            if res not in ls1:
                ls1.append(res)
                n = res
            else:
                break
        return True if n == 1 else False

    def add_sum(self, n):
        ls1 = [int(i) for i in str(n)]
        count = 0
        for i in ls1:
            count += i ** 2
        return count
