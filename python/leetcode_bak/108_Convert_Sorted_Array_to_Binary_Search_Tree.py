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
        # print(start, end)
        if start >= end:
            return TreeNode(nums[start])
        else:
            if end - start == 1:
                root = TreeNode(nums[end])
                root.left = TreeNode(nums[start])
                return root

            mid = int((start+end)/2)
            left = self.buffer(nums, start, mid-1)
            right = self.buffer(nums, mid+1, end)
            root = TreeNode(nums[mid])
            root.left = left
            root.right = right
            return root
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        end = len(nums) - 1
        if end < 0:
            return None
        return self.buffer(nums, 0, len(nums)-1)

def traverse(root):
    if root is not None:

        traverse(root.left)
        print(root.val, end="")
        traverse(root.right)



def main():
    s = Solution()
    root = s.sortedArrayToBST([-10,-3,0,5,9])
    traverse(root)
    root = s.sortedArrayToBST([])
    traverse(root)


if __name__ == "__main__":
    main()
