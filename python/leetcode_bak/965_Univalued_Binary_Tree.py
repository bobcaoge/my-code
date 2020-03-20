# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    flag = True
    old = 0

    def traverse(self, root):
        if root and self.flag:
            if root.val != self.old:
                self.flag = False
                return
            else:
                self.traverse(root.left)
                self.traverse(root.right)

    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.flag = True
        self.old = root.val
        self.traverse(root)
        return self.flag

def main():
    s = Solution()


if __name__ == "__main__":
    main()
