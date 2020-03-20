# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if root:
            left = self.trimBST(root.left, L, R)
            right = self.trimBST(root.right, L, R)
            if L <= root.val <= R:
                root.left = left
                root.right = right
                return root
            if root.val > R:
                return left
            if root.val < L:
                return right
        return None




def main():
    s = Solution()


if __name__ == "__main__":
    main()
