# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    ret = None
    def traverse2(self, root):
        if root:
            self.traverse2(root.right)
            root.right = self.ret
            if self.ret:
                self.ret.left = None
            self.ret = root
            self.traverse2(root.left)

    ret = None
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            self.traverse2(root.right)
            root.right = self.ret
            if self.ret:
                self.ret.left = None
            self.ret = root
            self.traverse2(root.left)
            return self.ret


def main():
    s = Solution()


if __name__ == "__main__":
    main()
