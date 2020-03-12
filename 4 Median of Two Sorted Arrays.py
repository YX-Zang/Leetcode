class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        list1 = sorted(nums1 + nums2)
        if len((list1)) % 2 == 1:
            return list1[int((len(list1)) / 2)]
        else:
            index1 = int(len(list1) / 2)
            return (list1[index1 - 1] + list1[index1]) / 2

