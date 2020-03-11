class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for index, string in enumerate(s[::-1]):
            asc = ord(string) - 64
            count = count + asc * 26 ** index
        return count

if __name__ == '__main__':
    # a = ord('A') - 64
    # b = ord('Z') - 64
    # print(a)
    # print(b)
    Solution = Solution()
    print(Solution.titleToNumber('ZY'))