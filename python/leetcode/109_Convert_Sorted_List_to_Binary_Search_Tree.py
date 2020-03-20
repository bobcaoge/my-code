# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


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

    def get_nums(self, head):
        ret = []
        while head:
            ret.append(head.val)
            head = head.next
        return ret

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        nums = self.get_nums(head)
        end = len(nums) - 1
        if end < 0:
            return None
        return self.buffer(nums, 0, len(nums)-1)

def main():
    s = Solution()


if __name__ == "__main__":
    main()
