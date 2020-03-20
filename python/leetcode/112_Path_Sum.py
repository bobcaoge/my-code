# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    flag = False
    target = 0
    def buffer(self,root,sum):
        """
        :type root: TreeNode
        :param root:
        :param sum:
        :return:
        """
        if self.flag:
            return

        if root is None:
            return
        else:
            sum += root.val
            if sum == self.target and root.left is None and root.right is None:
                self.flag = True
            else:
                self.buffer(root.left, sum)
                self.buffer(root.right, sum)
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.target = sum
        self.buffer(root, 0)
        return self.flag


def main():
    s = Solution()


if __name__ == "__main__":
    main()
