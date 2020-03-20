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
    def buffer(self,root, s):
        if root.left is None and root.right is None:
            if s == "":
                s_= str(root.val)
            else:
                s_= s+"->"+str(root.val)
            self.ret.append(s_)
            return
        if root.left is not None:
            if s == "":
                s_left= str(root.val)
            else:
                s_left= s+"->"+str(root.val)
            self.buffer(root.left, s_left)
        if root.right is not None:
            if s == "":
                s_right = str(root.val)
            else:
                s_right = s+"->"+str(root.val)
            self.buffer(root.right,s_right)
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        self.ret = []
        self.buffer(root,"")
        return self.ret





def main():
    s = Solution()


if __name__ == "__main__":
    main()
