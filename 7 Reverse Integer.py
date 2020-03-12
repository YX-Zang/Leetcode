class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # type 1
        # flag = 1 if x >= 0 else -1
        # x = abs(x)
        # return flag * int(str(x)[::-1])
        # --------------------------------------------------
        # type 2
        flag = 1 if x >= 0 else -1
        x = abs(x)
        new_x = 0
        while x > 0:
            new_x = new_x * 10 + x % 10
            x //=10
        if new_x > 2**31:
            return 0
        return flag * new_x


if __name__ == '__main__':
    Solution = Solution()
    print(Solution.reverse(123))
    print(Solution.reverse(-123))
    print(Solution.reverse(120))
