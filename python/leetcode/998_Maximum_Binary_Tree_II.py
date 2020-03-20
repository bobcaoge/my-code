# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)

        if root.val < val:
            ret = TreeNode(val)
            ret.left = root
            return ret
        root.right = self.insertIntoMaxTree(root.right, val)
        return root




def main():
    s = Solution()


if __name__ == "__main__":
    main()
