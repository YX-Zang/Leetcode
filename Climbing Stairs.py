class Solution:
    def climbStairs(self, n: int) -> int:
        # if n < 3:
        #     return n
        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            s1, s2 = 1, 2
            for _ in range(n - 2):
                s1, s2 = s2, s1 + s2
            return s2
