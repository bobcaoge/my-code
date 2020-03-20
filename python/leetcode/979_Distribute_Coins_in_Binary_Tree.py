# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def dfs(root):
            if not root:
                return 0
            L, R = dfs(root.left), dfs(root.right)
            self.ans += abs(L) + abs(R)
            return root.val + L + R - 1
        dfs(root)
        return self.ans





def main():
    s = Solution()


if __name__ == "__main__":
    main()
