class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A = 0
        b_l = []
        row_list = list(guess)
        chk_list = list(secret)
        for index, v in enumerate(row_list):
            if chk_list[index] == v:
                row_list[index] = '+'
                chk_list[index] = '-'
                A += 1
        for index, v in enumerate(row_list):
            if v in chk_list:
                index0 = chk_list.index(v)
                b_l.append(index0)
                chk_list[index0] = '-'
        return '%sA%sB' % (A, len(set(b_l)))
