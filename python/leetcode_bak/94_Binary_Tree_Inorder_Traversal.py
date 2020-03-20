# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    ret = []
    def traversal(self, root):
        if root:
            self.traversal(root.left)
            self.ret.append(root.val)
            self.traversal(root.right)
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.ret = []
        self.traversal(root)
        return self.ret


def main():
    s = Solution()


if __name__ == "__main__":
    main()
