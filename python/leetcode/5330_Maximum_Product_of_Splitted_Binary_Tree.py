# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxProduct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        m = {}
        to_mod = 10**9+7

        def dfs(r):
            if not r:
                return 0
            m[r] = dfs(r.left) + dfs(r.right)+r.val
            return m[r]
        sum_of_all_node = dfs(root)
        def compare(x, y):
            a, b = x
            c, d = y
            if a > c:
                return True
            if a < c:
                return False
            if b > d:
                return True
            return False

        self.ret = [0, 0]
        def dfs2(r):
            if r:
                first = m[r]
                second = sum_of_all_node-first
                a, b = divmod(first*second, to_mod)
                if compare([a, b], self.ret):
                    self.ret = [a, b]
                dfs2(r.left)
                dfs2(r.right)
        dfs2(root)
        return self.ret[-1]




def main():
    s = Solution()


if __name__ == "__main__":
    main()
