class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        str_len = len(needle)
        if needle in haystack:
            for index in range(0, len(haystack) - str_len + 1):
                if haystack[index: index + str_len] == needle:
                    return index
        else:
            return -1
