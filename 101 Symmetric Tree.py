# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.mirror(root.left, root.right)

    def mirror(self, L, R):
        if not L or not R:
            return L == R
        if L.val != R.val:
            return False
        return self.mirror(L.left, R.right) and self.mirror(L.right, R.left)