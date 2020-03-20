# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.depth = 0
        self.ret = 0
        def dfs(r, depth):
            if r:
                if depth > self.depth:
                    self.depth = depth
                    self.ret = r.val
                elif depth == self.depth:
                    self.ret += r.val
                dfs(r.left, depth+1)
                dfs(r.right, depth+1)
        dfs(root, 1)
        return self.ret


def main():
    s = Solution()


if __name__ == "__main__":
    main()
