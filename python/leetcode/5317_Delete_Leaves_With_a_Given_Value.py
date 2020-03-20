# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        def dfs(r):
            if r:
                r.left = dfs(r.left)
                r.right = dfs(r.right)
                if r.left is None and r.right is None and r.val == target:
                    return None
                return r
            return None
        return dfs(root)




def main():
    s = Solution()


if __name__ == "__main__":
    main()
