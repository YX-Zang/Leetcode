class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = dict()
        for index, value in enumerate(nums):
            sub = target - value
            if sub in dic:
                return [dic[sub], index]
            dic[value] = index


if __name__ == '__main__':
    Solution = Solution()
    print(Solution.twoSum([3, 2, 4], 6))
    print(Solution.twoSum([3, 3], 6))
    print(Solution.twoSum([2, 7, 11, 15], 9))
