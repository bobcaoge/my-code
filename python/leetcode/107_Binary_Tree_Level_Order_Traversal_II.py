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

    def tranverse(self, root, length = 0):
        if root is None:
            return
        # print(length, root.val)
        try:
            self.ret[length].append(root.val)
        except:
            self.ret.append([root.val])
        self.tranverse(root.left, length+1)
        self.tranverse(root.right, length+1)


    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.ret = []
        self.tranverse(root)
        start = 0
        end = len(self.ret)-1
        while start < end:
            self.ret[start], self.ret[end] = self.ret[end], self.ret[start]
            start += 1
            end -= 1
        return self.ret




def main():
    s = Solution()
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    # print(s.tranverse(root))
    # print(s.ret)
    print(s.levelOrderBottom(root))
    print(s.levelOrderBottom(None))

if __name__ == "__main__":
    main()
