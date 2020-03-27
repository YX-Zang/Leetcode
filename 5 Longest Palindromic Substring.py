class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
    #     if len(s) == 1:
    #         return s
    #     elif not s:
    #         return ''
    #     s1 = self.aa(s)
    #     s2 = self.aa(s[::-1])
    #     res1 = set(s1)&set(s2)
    #     if len(res1) == 1:
    #         return list(res1)[0]
    #     elif len(res1) > 1:
    #         # print(max(res1, key=len))
    #         # dic = dict()
    #         # for i in res1:
    #         #     dic.update({len(i):i})
    #         # return dic[max(dic)]
    #     else:
    #         return ''
    # def aa(self, s):
    #     return [s[i:j] for j in range(len(s)) for i in range(len(s)) if len(s[i:j]) > 1]
    #　------------------------------------------------------------------------------------
    #     res = ""
    #     for i in range(len(s)):
    #         res = max(self.max_substr(s, i, i), self.max_substr(s, i, i + 1), res, key=len)
    #     return res
    #
    # def max_substr(self, s, l, r):
    #     while l >= 0 and r < len(s) and s[l] == s[r]:
    #         l -= 1
    #         r += 1
    #     return s[l + 1:r]
    # 　------------------------------------------------------------------------------------
        if len(s) == 1:
            return s[0]
        elif not s:
            return ''
        ls1 = []


if __name__ == '__main__':
    Solution = Solution()
    print(Solution.longestPalindrome('babad'))
    # print(Solution.longestPalindrome('cbbd'))
    # print(Solution.longestPalindrome('a'))
    # print(Solution.longestPalindrome('aca'))