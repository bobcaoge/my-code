# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return TreeNode(val)
        cur = root
        while True:
            if val > cur.val:
                if cur.right is None:
                    cur.right = TreeNode(val)
                    break
                else:
                    cur = cur.right
            else:
                if cur.left is None:
                    cur.left = TreeNode(val)
                    break
                else:
                    cur = cur.left
        return root


def main():
    s = Solution()


if __name__ == "__main__":
    main()
