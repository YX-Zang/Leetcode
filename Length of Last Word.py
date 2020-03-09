class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s2 = s.split(' ')
        s3 = [s for s in s2 if s]
        return len(s3[-1]) if s3 else 0
