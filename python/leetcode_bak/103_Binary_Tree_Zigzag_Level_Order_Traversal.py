# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    m = []


    def traversal(self, root, depth):
        """
        :type root: TreeNode
        :type depth: int
        :rtype: void
        """
        if root:
            if depth >= len(self.m):
                self.m.append([root.val])
            else:
                self.m[depth].append(root.val)
            self.traversal(root.left, depth + 1)
            self.traversal(root.right, depth + 1)

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.m = []
        self.traversal(root, 0)
        for index, level in enumerate(self.m):
            if index % 2 == 1:
                self.m[index] = level[-1::-1]
        return self.m




def main():
    s = Solution()


if __name__ == "__main__":
    main()
