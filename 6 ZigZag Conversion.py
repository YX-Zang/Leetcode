class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) == 0:
            return ''
        elif numRows == 1:
            return s
        else:
            ls1 = []
            if len(s) // numRows == 0:
                return s
            for j in range(len(s) // numRows):
                for i in range(numRows):
                    base = 2 * (numRows - 1) * j
                    if (base + i) >= len(s):
                        break
                    elif (base + 2 * (numRows - 1) - i) >= len(s):
                        ls1.append((base + i))
                    else:
                        ls1.append((base + i, base + 2 * (numRows - 1) - i))
            ls2 = []
            for i in range(numRows):
                for x in ls1[i::numRows]:
                    if isinstance(x, tuple):
                        if x[0] not in ls2:
                            ls2.append(x[0])
                        if x[1] not in ls2:
                            ls2.append(x[1])
                    else:
                        if x not in ls2:
                            ls2.append(x)
            return ''.join([s[i] for i in ls2])
