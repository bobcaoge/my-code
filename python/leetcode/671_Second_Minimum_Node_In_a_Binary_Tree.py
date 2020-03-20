# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    first = 0
    second = 0

    def update(self, value):

        if value < self.first:
            self.second = self.first
            self.first = value
        elif self.first < value < self.second:
            self.second = value

    def traverse1(self, root):
        if root is None:
            return 2**32
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        if root.val <= left and root.val <= right:
            self.update(root.val)
        return root.val

    def traverse(self, root):
        if root is None:
            return 2**32
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        if root.val <= left and root.val <= right:
            if root.val < self.first:
                self.second = self.first
                self.first = root.val
            elif self.first < root.val < self.second:
                self.second = root.val
        return root.val

    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.first = self.second = 2**32
        self.traverse(root)
        return self.second if self.second != 2**32 else -1


def main():
    s = Solution()


if __name__ == "__main__":
    main()
