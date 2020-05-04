# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        s = ''
        if not head:
            return True
        ls1 = []
        while head != None:
            ls1.append(head.val)
            head = head.next
        return ls1 == ls1[::-1]