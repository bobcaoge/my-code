# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    m = {}
    max_depth = 0

    def traversal(self, root, depth):
        """
        :type root: TreeNode
        :type depth: int
        :rtype: void
        """
        if root:
            self.m[depth] = self.m.get(depth, []) + [root.val]
            self.max_depth = max(self.max_depth, depth)
            self.traversal(root.left, depth + 1)
            self.traversal(root.right, depth + 1)

    def levelOrder1(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.m = {}
        self.max_depth = 0
        self.traversal(root, 0)
        ret = []
        if not root:
            return ret
        for i in range(self.max_depth + 1):
            ret.append(self.m[i])
        return ret

    def levelOrder(self, root, depth=0, m=[]):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if depth == 0:
            m = []
        if root:
            if depth >= len(m):
                m.append([root.val])
            else:
                m[depth].append(root.val)
            self.levelOrder(root.left, depth + 1, m)
            self.levelOrder(root.right, depth + 1, m)
        return m


def main():
    s = Solution()


if __name__ == "__main__":
    main()
