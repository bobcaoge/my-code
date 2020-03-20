# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def same(self, s, t):
        """
        :type s:TreeNode
        :type t:TreeNode
        :rtype: bool
        """
        if not s and not t:
            return True
        elif (not s and t) or (not t and s):
            return False
        else:
            return self.same(s.left, t.left) and self.same(s.right, t.right) if s.val == t.val else False

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if self.same(s,t):
            return True
        left = right = False
        if s.left:
            left = self.isSubtree(s.left, t)
        if s.right:
            right = self.isSubtree(s.right, t)
        return left or right




def main():
    s = Solution()


if __name__ == "__main__":
    main()
