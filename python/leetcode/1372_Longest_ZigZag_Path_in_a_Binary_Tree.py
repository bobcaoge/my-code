# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(direction, depth, r):
            """
            :type direction: int  0 stands for left, 1 stands for right
            :type depth: int
            :type r: TreeNode
            :return: int
            """
            if not r:
                return depth
            left = right = 0
            if direction == 0:
                left = dfs(0, 0, r.left)
                right = dfs(1, depth+1, r.right)
            elif direction == 1:
                left = dfs(0, depth+1, r.left)
                right = dfs(1, 0, r.right)
            return max(left, right, depth)
        return max(dfs(0, 0, root.left), dfs(1, 0, root.right) )



def main():
    s = Solution()


if __name__ == "__main__":
    main()
