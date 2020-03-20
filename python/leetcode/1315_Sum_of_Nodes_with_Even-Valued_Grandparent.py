# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def get_sum(r):
            if not r:
                return 0
            res = 0
            res += r.left.val if r.left else 0
            res += r.right.val if r.right else 0
            return res
        self.ret = 0
        def dfs(r):
            if r:
                if r.val % 2 == 0:
                    self.ret += get_sum(r.left) + get_sum(r.right)
                dfs(r.left)
                dfs(r.right)
        dfs(root)
        return self.ret



def main():
    s = Solution()


if __name__ == "__main__":
    main()
