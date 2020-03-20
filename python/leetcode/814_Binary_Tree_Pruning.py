# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(r):
            if not r:
                return False
            left = dfs(r.left)
            right = dfs(r.right)
            if not left:
                r.left = None
            if not right:
                r.right = None
            return r.val == 1 or left or right

        return root if dfs(root) else None



def main():
    s = Solution()


if __name__ == "__main__":
    main()
