# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    root = None
    flag = False
    def find(self, root, target):
        """
        :type root: TreeNode
        :param root:
        :param target:
        :return:
        """
        if root:
            if target == root.val:
                return root
            elif target > root.val:
                return self.find(root.right, target)
            else:
                return self.find(root.left, target)
        return None

    def findTargetBuffer(self, root, k):
        if root and not self.flag:
            next_num = k - root.val
            result = self.find(self.root, next_num)
            if result and result != root:
                # print(root.val, result.val)
                self.flag = True
                return True
            left = self.findTargetBuffer(root.left, k)
            right = self.findTargetBuffer(root.right, k)
            return left or right
        return False

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.root = root
        self.flag = False
        # print(self.find(self.root, 1))
        return self.findTargetBuffer(root, k)

def main():
    s = Solution()
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(s.findTarget(root, 4))


if __name__ == "__main__":
    main()
