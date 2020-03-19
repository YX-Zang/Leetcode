class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dic = {5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        s = ''
        while num:
            if num >= 1000:
                s += dic[1000]
                num -= 1000
            elif num >= 500:
                s += dic[500]
                num -= 500
            elif num >= 100:
                s += dic[100]
                num -= 100
            elif num >= 50:
                s += dic[50]
                num -= 50
            elif num >= 10:
                s += dic[10]
                num -= 10
            elif num >= 5:
                s += dic[5]
                num -= 5
            else:
                s += 'I'
                num -= 1
        s = s.replace('DCCCC', 'CM')
        s = s.replace('CCCC', 'CD')
        s = s.replace('LXXXX', 'XC')
        s = s.replace('XXXX', 'XL')
        s = s.replace('VIIII', 'IX')
        s = s.replace('IIII', 'IV')
        return s

