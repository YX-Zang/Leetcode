class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ls1 = [dic[i] for i in s]
        for i in range(len(ls1)-1, 0, -1):
            if ls1[i] > ls1[i-1]:
                ls1[i-1] = ls1[i-1] * -1
        return sum(ls1)
