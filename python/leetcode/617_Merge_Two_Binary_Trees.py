# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2:
            t1.val += t2.val
            if t1.left and t2.left:
                self.mergeTrees(t1.left, t2.left)
            elif not t1.left and t2.left:
                t1.left = t2.left

            if t1.right and t2.right:
                self.mergeTrees(t1.right, t2.right)
            elif not t1.right and t2.right:
                t1.right = t2.right
        return t1 or t2


def main():
    s = Solution()


if __name__ == "__main__":
    main()
