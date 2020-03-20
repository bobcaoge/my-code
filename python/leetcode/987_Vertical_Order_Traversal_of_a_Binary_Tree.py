# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    left = []
    right = []

    def insert(self, nums, to_insert, depth_of_to_insert):
        """
        :type nums: list
        :type to_insert: int
        :param nums:
        :param to_insert:
        :return:
        """
        for index, num in enumerate(nums):
            if depth_of_to_insert < num[1]:
                nums.insert(index, (to_insert, depth_of_to_insert))
                return
            elif depth_of_to_insert == num[1]:
                if to_insert <= num[0]:
                    nums.insert(index, (to_insert, depth_of_to_insert))
                    return
        nums.append((to_insert, depth_of_to_insert))

    def storage(self, root, position=0, depth=0):
        """
        :type root: TreeNode
        :param root:
        :param position:
        :return:
        """
        if not root:
            return
        if root:
            if position >=0:
                if len(self.right) > position:
                    self.insert(self.right[position], root.val, depth)
                else:
                    self.right.append([(root.val, depth)])
            else:
                if len(self.left) > -position - 1:
                    self.insert(self.left[-position - 1], root.val, depth)
                else:
                    self.left.append([(root.val, depth)])
        self.storage(root.left, position-1, depth+1)
        self.storage(root.right, position+1, depth+1)

    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.left = []
        self.right = []
        self.storage(root)
        length = len(self.left)
        start = 0
        end = length -1
        while start < end:
            self.left[start], self.left[end] = self.left[end], self.left[start]
            start += 1
            end -=1
        ret = []
        for ver in self.left + self.right:
            buffer = []
            for num in ver:
                buffer.append(num[0])
            ret.append(buffer)
        return ret





def main():
    s = Solution()


if __name__ == "__main__":
    main()
