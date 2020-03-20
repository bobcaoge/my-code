# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    level_sums = []

    def traverse(self, root, depth):
        if root:
            if len(self.level_sums)-1 < depth:
                self.level_sums.append(0)
            self.level_sums[depth] += root.val
            self.traverse(root.left, depth+1)
            self.traverse(root.right, depth+1)

    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.level_sums = []
        self.traverse(root, 0)
        i = 0
        max_sum = 0
        for index, sum_ in enumerate(self.level_sums):
            if sum_ > max_sum:
                i, max_sum = index, sum_
        return i+1




def main():
    s = Solution()


if __name__ == "__main__":
    main()
