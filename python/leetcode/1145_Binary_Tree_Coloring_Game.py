# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def btreeGameWinningMove(self, root, n, x):
        """
        :type root: TreeNode
        :type n: int
        :type x: int
        :rtype: bool
        """
        self.children = []
        def get(root):
            if not root:
                return 0
            left = get(root.left)
            right = get(root.right)
            if root.val == x:
                self.children = [left, right]
            return left + right + 1
        get(root)
        left, right = self.children
        up = n - sum(self.children)
        return left > n//2 or right > n//2 or up > n//2





def main():
    s = Solution()


if __name__ == "__main__":
    main()
