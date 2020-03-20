# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buffer(self, root, left_flag):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            if left_flag:
                return root.val
            else:
                return 0
        x = 0
        y = 0
        if root.left is not None:
            x = self.buffer(root.left, True)
        if root.right is not None:
            y = self.buffer(root.right, False)
        return x+y


    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.buffer(root, False)


def main():
    s = Solution()


if __name__ == "__main__":
    main()
