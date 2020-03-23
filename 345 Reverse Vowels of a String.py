class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        ls1 = []
        for index, v in enumerate(s):
            if v.lower() in ['a', 'e', 'i', 'o', 'u']:
                ls1.append(index)
        ls1_rev = ls1[::-1]
        s2 = list(s)
        for i in range(len(ls1)):
            s2[ls1_rev[i]] = s[ls1[i]]
        return ''.join(s2)