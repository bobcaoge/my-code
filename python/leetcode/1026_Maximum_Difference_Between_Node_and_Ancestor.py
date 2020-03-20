# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ret = 0

        def dfs(root):
            if root:
                children = []
                children.extend(dfs(root.left))
                children.extend(dfs(root.right))
                if not children:
                    return [root.val, root.val]
                self.ret = max(self.ret, abs(root.val-min(children)), abs(root.val-max(children)))
                children.append(root.val)
                return [min(children), max(children)]
            return []
        dfs(root)
        return self.ret




def main():
    s = Solution()


if __name__ == "__main__":
    main()
