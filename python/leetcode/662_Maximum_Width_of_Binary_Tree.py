# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        m = []

        def traverse(root, depth, value):
            if root:
                if depth >= len(m):
                    m.append([])
                m[depth].append(value)
                traverse(root.left, depth+1, value << 1)
                traverse(root.right, depth+1, (value << 1)+1)
        traverse(root, 0, 0)
        ret = 0
        for row in m:
            ret = max(row[-1] - row[0]+1, ret)
        return ret



def main():
    s = Solution()


if __name__ == "__main__":
    main()
