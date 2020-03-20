# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    max_diameter = 0

    def traverse(self, root):
        if not root:
            return 0
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        cur_diameter = left+1+right
        if cur_diameter > self.max_diameter:
            self.max_diameter = cur_diameter
        return max(left, right)+1

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_diameter = 0
        self.traverse(root)
        return self.max_diameter-1 if self.max_diameter > 0 else 0


def main():
    s = Solution()


if __name__ == "__main__":
    main()
