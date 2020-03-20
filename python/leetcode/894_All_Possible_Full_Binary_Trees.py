# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N == 1:
            return [TreeNode(0)]
        ret = []
        for i in range(1, N-1, 2):
            for left in self.allPossibleFBT(i):
                for right in self.allPossibleFBT(N-i-1):
                    cur = TreeNode(0)
                    cur.left = left
                    cur.right = right
                    ret.append(cur)
        return ret






def main():
    s = Solution()


if __name__ == "__main__":
    main()
