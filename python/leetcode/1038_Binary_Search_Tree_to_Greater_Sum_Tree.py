# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.val = 0
        def dfs(root):
            if not root:
                return 0
            dfs(root.right)
            self.val += root.val
            root.val = self.val
            dfs(root.left)
            return root.val
        dfs(root)
        return root




def main():
    s = Solution()


if __name__ == "__main__":
    main()
