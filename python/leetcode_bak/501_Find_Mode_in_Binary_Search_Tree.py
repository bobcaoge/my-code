# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def traverse(self, root):
        if not root:
            return []
        return self.traverse(root.left)+[root.val]+self.traverse(root.right)


    def findMode1(self, root: 'TreeNode') -> 'List[int]':
        result = self.traverse(root)
        print(result)
        if len(result) == 1:
            return result

        cur_length = 0
        cur_c = result[0]
        max_length = 0
        max_c = []
        for c in result:
            if c == cur_c:
                cur_length += 1
            else:
                if cur_length > max_length:
                    max_c = [int(cur_c)]
                    max_length = cur_length
                elif cur_length == max_length:
                    max_c.append(int(cur_c))
                cur_c = c
                cur_length = 1
        if cur_length > max_length:
            max_c = [int(cur_c)]
            max_length = cur_length
        elif cur_length == max_length:
            max_c.append(int(cur_c))
        return max_c

    def get_num(self, root, value):
        if not root:
            return [[value], 0]
        left = self.get_num(root.left, value)[1]
        right = self.get_num(root.right, value)[1]
        if root.val == value:
            return [[value], left+right+1]
        else:
            return [[value], left+right]

    def traverse2(self, root):
        if root:
            cur = self.get_num(root, root.val)
            print(cur)
            left = self.traverse2(root.left) if root.left else [[0], 0]
            right = self.traverse2(root.right) if root.right else [[0], 0]
            if cur[1] < left[1]:
                cur = left
            elif cur[1] == left[1]:
                cur[0] += left[0]
            if cur[1] < right[1]:
                cur = right
            elif cur[1] == right[1]:
                cur[0] += right[0]
            return cur

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        return self.traverse2(root)[0]

def main():
    s = Solution()


if __name__ == "__main__":
    main()
