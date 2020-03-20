# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    abs_diff = 0
    last = 0
    def traverse(self, root):
        if root:
            self.traverse(root.left)
            if self.last != -1:
                self.abs_diff =min(abs(root.val - self.last), self.abs_diff)
            self.last = root.val
            print(self.last)
            self.traverse(root.right)

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left:
            self.abs_diff = abs(root.val - root.left.val)
        else:
            self.abs_diff = abs(root.val - root.right.val)
        self.last = -1
        self.traverse(root)
        return self.abs_diff


def main():
    s = Solution()


if __name__ == "__main__":
    main()
