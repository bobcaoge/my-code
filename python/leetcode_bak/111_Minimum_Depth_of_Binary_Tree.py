# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        length_left = self.minDepth(root.left)
        length_right = self.minDepth(root.right)
        if length_left != 0 and length_right != 0:
            return min(length_left, length_right) + 1
        elif length_right != 0:
            return length_right + 1
        else:
            return length_left+1



def main():
    s = Solution()


if __name__ == "__main__":
    main()
