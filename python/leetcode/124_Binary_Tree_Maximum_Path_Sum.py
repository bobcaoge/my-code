# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ret = root.val
        self.max_num = -1<<31
        def dfs(r):
            if not r:
                return 0
            self.max_num = max(self.max_num, r.val)
            left = dfs(r.left)
            right = dfs(r.right)
            self.ret = max(self.ret, max(left, 0)+max(right, 0)+r.val)
            return max(left+r.val, right+r.val, 0)
        dfs(root)
        if self.ret == 0:
            return self.max_num
        return self.ret





def main():
    s = Solution()


if __name__ == "__main__":
    main()
