class Solution:
    def divide(self, dividend, divisor):
        result = abs(dividend)//abs(divisor)
        if result >= 2**31:
            if dividend < 0 and divisor < 0:
                return 2**31 -1
            elif dividend < 0 or divisor < 0:
                return 2**31 * -1
            else:
                return 2**31 -1
        if dividend < 0 and divisor < 0:
            return result
        elif dividend < 0 or divisor < 0:
            return result * -1
        else:
            return result