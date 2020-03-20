# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        m = collections.defaultdict(list)
        def dfs(root, val, depth):
            if root:
                m[depth].append(val)
                dfs(root.left, val<<1, depth+1)
                dfs(root.right, (val<<1)+1, depth+1)

        dfs(root,0,1)
        for i in range(1, max(m.keys())):
            if len(m[i]) != (1<<i):
                return False
        buff = m[max(m.keys())]
        return sum(buff) == (len(buff)-1)*len(buff)/2





def main():
    s = Solution()


if __name__ == "__main__":
    main()
