# /usr/bin/python3.6
# -*- coding:utf-8 -*-

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution(object):
    def create_prefix_tree(self, nums):
        head = Node(0)
        for num in nums:
            cur = head
            for i in range(31, -1, -1):
                to_insert = 0 if num & (1 << i) == 0 else 1
                # print(to_insert, end="")
                if to_insert == 0 :
                    if cur.right is None:
                        cur.right = Node(0)
                    cur = cur.right
                elif to_insert == 1:
                    if cur.left is None:
                        cur.left = Node(1)
                    cur = cur.left
            # print()
        return head

    def traverse(self, root, value=0, depth=0):
        if root:
            add = 1 << (32-depth) if root.value == 1 else 0
            if root.left is None and root.right is None:
                print(value + add)
                return
            self.traverse(root.left, value + add, depth+1)
            self.traverse(root.right, value + add, depth+1)


    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        head = self.create_prefix_tree(nums)
        # self.traverse(head)
        max_num = -1

        for num in nums:
            cur = head
            cur_num = 0
            move = head
            for i in range(31, -1, -1):
                to_insert = 0 if num & (1 << i) == 0 else 1
                if to_insert == 0:
                    if move.left:
                        cur_num += (1 << i)
                        move = move.left
                    else:
                        move = move.right
                    cur = cur.right
                else:
                    if move.right:
                        cur_num += (1 << i)
                        move = move.right
                    else:
                        move = move.left
                    cur = cur.left
            max_num = max(max_num, cur_num)
        return max_num



def main():
    s = Solution()
    print(s.findMaximumXOR([3, 10, 5, 25, 2, 8]))


if __name__ == "__main__":
    main()
