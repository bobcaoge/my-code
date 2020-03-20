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
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if self.flag is False:
            return self.flag
        if p is None and q is not None:
            self.flag = False
            return self.flag
        elif p is not None and q is None:
            self.flag = False
            return self.flag
        elif p is not None and q is not None:
            if p.val == q.val:
                self.isSameTree(p.left, q.left)
                self.isSameTree(p.right, q.right)
                return self.flag
            else:
                self.flag = False
                return self.flag

        else:
            return self.flag


def main():
    s = Solution()
    q = TreeNode(1)
    q.right = TreeNode(1)
    q.left = TreeNode(2)
    p = TreeNode(1)
    p.right = TreeNode(2)
    p.left = TreeNode(1)
    s.isSameTree(q, p)
    print(s.flag)


if __name__ == "__main__":
    main()
