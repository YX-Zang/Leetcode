class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        s = ''.join(str(i) for i in b)
        s1 = int(s)
        return pow(a, s1, 1337)
