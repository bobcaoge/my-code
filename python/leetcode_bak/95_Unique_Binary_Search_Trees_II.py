# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def buffer(self, nums, start, end):
            roots = []
            for mid in range(start, end+1):
                lefts = self.buffer(nums, start, mid-1)
                rights = self.buffer(nums, mid+1, end)
                if lefts and rights:
                    for left in lefts:
                        for right in rights:
                            root = TreeNode(nums[mid])
                            root.left = left
                            root.right = right
                            roots.append(root)
                elif lefts:
                    for left in lefts:
                        root = TreeNode(nums[mid])
                        root.left = left
                        roots.append(root)
                elif rights:
                    for right in rights:
                        root = TreeNode(nums[mid])
                        root.right = right
                        roots.append(root)
                else:
                    root = TreeNode(nums[mid])
                    roots.append(root)
            return roots

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        self.length = n
        nums = [i+1 for i in range(n)]
        end = n - 1
        if end < 0:
            return []
        return self.buffer(nums, 0, n-1)


def main():
    s = Solution()
    ret = s.generateTrees(3)
    # print(ret)
    for node in ret:
        print(node.val)


if __name__ == "__main__":
    main()
