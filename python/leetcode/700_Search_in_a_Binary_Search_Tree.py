# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root:
            if root.val == val:
                return root
            if root.val < val:
                return self.searchBST(root.right, val)
            else:
                return self.searchBST(root.left, val)
        return root


def main():
    s = Solution()


if __name__ == "__main__":
    main()
