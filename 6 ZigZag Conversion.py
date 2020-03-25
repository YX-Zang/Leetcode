class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        print(s)
        print(numRows)
        for j in range(len(s)//numRows):
            for i in range(numRows):
                print(2*(numRows-1)*j+i, 2*(numRows-1)*j+2*(numRows-1)-i)




if __name__ == '__main__':
    Solution = Solution()
    # s = 'PAYPALISHIRING'
    s = 'PAYPALISHIRING'
    # print(len(s))
    numRows = 3
    # numRows = 4
    print(Solution.convert(s, numRows))