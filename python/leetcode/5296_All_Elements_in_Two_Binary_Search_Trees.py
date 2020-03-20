# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        self.ret = []
        def dfs(r):
            if r:
                self.ret.append(r.val)
                dfs(r.left)
                dfs(r.right)
        dfs(root1)
        dfs(root2)
        return sorted(self.ret) if self.ret else []



def main():
    s = Solution()


if __name__ == "__main__":
    main()
