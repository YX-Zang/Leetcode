class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ls1 = []
        for i in range(1, n+1):
            s = ''
            if i % 5 == 0 or i % 3 == 0:
                if i % 3 ==0:
                    s += 'Fizz'
                if i % 5 == 0:
                    s += 'Buzz'
            else:
                s += '%s' % i
            ls1.append(s)
        return ls1
