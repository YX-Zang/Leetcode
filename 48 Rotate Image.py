class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix[0])
        ls0 = []
        for i in matrix:
            ls0 += i
        matrix[:] = [ls0[i::length][::-1] for i in range(length)]
