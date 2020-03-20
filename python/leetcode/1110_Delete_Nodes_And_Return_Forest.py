# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        self.ret = []
        to_delete = set(to_delete)
        def dfs(root, parent):
            if not root:
                return
            if root.val in to_delete:
                if parent and parent.left == root:
                    parent.left = None
                if parent and parent.right == root:
                    parent.right = None

                if root.left and root.left.val not in to_delete:
                    self.ret.append(root.left)
                if root.right and root.right.val not in to_delete:
                    self.ret.append(root.right)
            dfs(root.left, root)
            dfs(root.right, root)
        dfs(root, None)
        if root and root.val not in to_delete:
            self.ret.append(root)
        return self.ret


def main():
    s = Solution()


if __name__ == "__main__":
    main()
