# from collections import Counter
class Solution(object):
    def longestCommonPrefix(self, strs):
        s = ''
        for string in zip(*strs):
            tmp = list(set(string))
            if len(tmp) == 1:
                s += tmp[0]
            else:
                break
        return s

