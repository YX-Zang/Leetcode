import itertools
class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        ls1 = []
        for i in itertools.permutations(A):
            hour = i[0]*10 + i[1]
            minute = i[2]*10 + i[3]
            if hour < 24 and minute < 60:
                ls1.append((hour, minute))
            else:
                continue
        return '%02d:%02d' % (max(ls1)[0], max(ls1)[1]) if ls1 else ''
