class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # print(zip(l1, l2))
        if not l1:
            return l2
        if not l2:
            return l1
        if (l1.val <= l2.val):
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
if __name__ == '__main__':
    Solution = Solution()
    l1 = [1, 2, 4]
    l2 = [1, 3, 4]
    print(Solution.mergeTwoLists(l1, l2))
