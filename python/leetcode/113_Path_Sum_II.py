# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    ret = []
    target = 0
    root = None

    def traverse(self, root, path, sum_of_path):
        if root:
            sum_of_path += root.val

            if not root.left and not root.right:
                if sum_of_path == self.target:
                    self.ret.append(path+[root.val])
            else:
                if root.left:
                    self.traverse(root.left, path+[root.val], sum_of_path)
                if root.right:
                    self.traverse(root.right, path+[root.val], sum_of_path)

    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: List[List[int]]
        """
        self.ret = []
        self.root = root
        self.target = target
        self.traverse(root, [], 0)
        return self.ret


def main():
    s = Solution()


if __name__ == "__main__":
    main()
