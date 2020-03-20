# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def temp(self, root):
        if root.right is None and root.left is None:
            return [root.val, str(chr(root.val+97))]
        elif root.left is None and root.right is not None:
            buffer = self.temp(root.right)
            buffer[0] += root.val
            buffer[1] += str(chr(root.val+97))
            return buffer
        elif root.right is None and root.left is not None:
            buffer = self.temp(root.left)
            buffer[0] += root.val
            buffer[1] += str(chr(root.val+97))
            return buffer
        else:
            left = self.temp(root.left)
            right = self.temp(root.right)

            buffer = left if left[1] < right[1] else right
            print()
            buffer[0] += root.val
            buffer[1] += str(chr(root.val+97))
            return buffer

    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        if root.right is None and root.left is None:
            return str(chr(root.val + 97))
        elif root.left is None and root.right is not None:
            buffer = self.smallestFromLeaf(root.right)
            buffer += str(chr(root.val + 97))
            return buffer
        elif root.right is None and root.left is not None:
            buffer = self.smallestFromLeaf(root.left)
            buffer += str(chr(root.val + 97))
            return buffer
        else:
            left = self.smallestFromLeaf(root.left)
            right = self.smallestFromLeaf(root.right)

            buffer = left if left < right else right
            buffer += str(chr(root.val + 97))
            return buffer



def main():
    s = Solution()
    root = TreeNode(25)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(2)
    print(s.smallestFromLeaf(root))


if __name__ == "__main__":
    main()
