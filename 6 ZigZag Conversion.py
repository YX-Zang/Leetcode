class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        print(s)
        print(numRows)
        ls1 = []
        for j in range(len(s)//numRows):
            for i in range(numRows):
                base = 2*(numRows-1)*j
                if (base+i) >= len(s):
                    # print('1~~~~~',base + i, base + 2 * (numRows - 1) - i)
                    break
                elif (base + 2 * (numRows - 1) - i) >= len(s):
                    # print('2~~~~~',base + i, base + 2 * (numRows - 1) - i)
                    # print('2~~~~~',base + i)
                    # ls1.append((i, (base+i)))
                    ls1.append((base+i))
                else:
                    # print(base + i, base + 2 * (numRows - 1) - i)
                    # if base + i == base + 2 * (numRows - 1) - i:
                    #     ls1.append((i,(base + i)))
                    # else:
                    # ls1.append((i, (base + i, base + 2 * (numRows - 1) - i)))
                    ls1.append((base + i, base + 2 * (numRows - 1) - i))
                    # ls1.append((base + i))
                    # if (base+i) not in ls1:
                    #     ls1.append((base+i))
                    # if (base+2*(numRows - 1)-i) not in ls1:
                    #     ls1.append(base+2*(numRows - 1)-i)
        print(ls1)
        ls2 = []
        for i in range(numRows):
            print(ls1[i::numRows])
            # ls2.extend([s[x] for x in ls1[i::numRows]])
        print(ls2)
        # return ''.join(ls2)


if __name__ == '__main__':
    Solution = Solution()
    # s = 'PAYPALISHIRING'
    s = 'PAYPALISHIRING'
    # print(len(s))
    numRows = 3
    # numRows = 4
    print(Solution.convert(s, numRows))