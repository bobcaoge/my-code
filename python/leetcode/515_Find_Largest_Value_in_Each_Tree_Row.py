# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):

     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        def traverse(root, depth):
            if root:
                if len(ret) <= depth:
                    ret.append(root.val)
                else:
                    ret[depth] = max(ret[depth], root.val)
                traverse(root.left, depth+1)
                traverse(root.right, depth+1)
        traverse(root, 0)
        return ret



def main():
    s = Solution()


if __name__ == "__main__":
    main()
