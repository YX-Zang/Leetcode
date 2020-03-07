class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        count = 0
        list1 = [dic[string] for string in s]
        for index in range(len(list1)-1):
            if list1[index] < list1[index+1]:
                list1[index] *= -1
            count+= list1[index]
        count += list1[len(list1)-1]
        return count
