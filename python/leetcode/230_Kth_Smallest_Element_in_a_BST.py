# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    cur_place = 0
    k = 0
    ret = 0
    def traverse(self, root):
        if root:
            self.k += 1
            self.traverse(root.left)
            if self.cur_place == self.k:
                self.ret = root.val
                return
            self.traverse(root.right)

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.cur_place = 0
        self.k = k
        self.traverse(root)
        return self.ret




def main():
    s = Solution()


if __name__ == "__main__":
    main()
