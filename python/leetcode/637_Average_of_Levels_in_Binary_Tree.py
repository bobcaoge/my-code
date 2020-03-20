# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    ret = []

    def traverse(self, root, depth=0):
        """
        :type root: TreeNode
        :param root:
        :return:
        """
        if root:
            if depth < len(self.ret):
                buffer = self.ret[depth]
                self.ret[depth][0] = (buffer[0]*buffer[1] + root.val)/(buffer[1]+1)
                self.ret[depth][1] += 1
            else:
                self.ret.append([root.val, 1])
            self.traverse(root.left, depth+1)
            self.traverse(root.right, depth+1)

    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        self.ret = []
        self.traverse(root,)
        return [x[0]*1.0 for x in self.ret]


def main():
    s = Solution()


if __name__ == "__main__":
    main()
