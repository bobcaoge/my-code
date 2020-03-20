# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    nums = {}
    max_count = 0
    def traverse(self, root):
        """
        :type root: TreeNode
        :return:
        """
        if root:
            left = self.traverse(root.left)
            right = self.traverse(root.right)
            result = left+right+root.val
            self.nums[result] = self.nums.get(result, 0) + 1
            self.max_count = max(self.nums[result], self.max_count)
            return result
        return 0

    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.nums = {}
        self.max_count = 0
        self.traverse(root)
        ret = []

        for num, count in self.nums.items():
            if count == self.max_count:
                ret.append(num)
        return ret



def main():
    s = Solution()


if __name__ == "__main__":
    main()
