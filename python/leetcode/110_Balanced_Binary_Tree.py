# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    flag = True
    def buffer(self, root):
        if not self.flag:
            return 0
        if root is None:
            return 0
        length_left = self.buffer(root.left)
        length_right = self.buffer(root.right)
        if abs(length_right-length_left) <= 1:
            return max(length_left, length_right) + 1
        else:
            self.flag = False
            return 0

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.buffer(root)
        return self.flag




def main():
    s = Solution()


if __name__ == "__main__":
    main()
