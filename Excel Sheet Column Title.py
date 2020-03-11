class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        string = ''
        while True:
            if n > 26:
                sqr = n//26
                n = n - sqr * 26
                string += chr(sqr + 64)
            elif n == 26:
                string += chr(n % 27 + 64)
                break
            else:
                string += chr(n % 26 + 64)
                break
        return string

if __name__ == '__main__':
    Solution = Solution()
    print(Solution.convertToTitle(52))
    # print(28//26)
