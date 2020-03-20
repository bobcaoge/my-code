# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    ret = []
    def preorder(self, root, depth):
        if root:
            if depth < len(self.ret):
                self.ret[depth] = root.val
            else:
                self.ret.append(root.val)
            self.preorder(root.left, depth+1)
            self.preorder(root.right, depth+1)
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.ret = []
        self.preorder(root, 0)
        return self.ret



def main():
    s = Solution()


if __name__ == "__main__":
    main()
