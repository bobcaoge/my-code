# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    ret = 2**32
    cur = 2**32
    def traverse(self, root):
        if root:
            self.traverse(root.left)
            if self.cur == 2**32:
                self.cur = root.val
            else:
                self.ret = min(self.ret, root.val - self.cur)
                self.cur = root.val
            self.traverse(root.right)


    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ret = 2**32
        self.cur = 2**32
        self.traverse(root)
        return self.ret


def main():
    s = Solution()


if __name__ == "__main__":
    main()
