# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def get(arr, start, end):
            index = start
            for i in range(start, end+1):
                if arr[i] > arr[index]:
                    index = i
            return index

        def construct(arr, start, end):
            if start == end:
                return TreeNode(nums[start])
            elif start > end:
                return None
            else:
                index = get(arr, start, end)
                cur_node = TreeNode(arr[index])
                cur_node.left = construct(arr, start, index-1)
                cur_node.right = construct(arr, index+1, end)
                return  cur_node
        return construct(nums, 0, len(nums)-1)



def main():
    s = Solution()


if __name__ == "__main__":
    main()
