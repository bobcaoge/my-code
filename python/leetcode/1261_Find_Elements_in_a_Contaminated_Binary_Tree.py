# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class FindElements(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.vals = set()
        def dfs(r, val):
            if r:
                r.val = val
                self.vals.add(val)
                dfs(r.left, (val<<1)+1)
                dfs(r.right, (val<<1)+2)
        dfs(root, 0)

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return target in self.vals



# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)


def main():
    pass


if __name__ == "__main__":
    main()
