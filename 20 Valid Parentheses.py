class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        elif len(s) % 2 == 1:
            return False
        dic = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for char in s:
            if char in '([{':
                stack.append(dic[char])
            elif stack:
                if char == stack[-1]:
                    stack.pop()
            else:
                return False
        return len(stack) == 0

