# /usr/bin/python3.6
# -*- coding:utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


class Solution(object):
    def get_fathers(self, root, target):
        if root:
            if root == target:
                return [root]
            left = self.get_fathers(root.left, target)
            right = self.get_fathers(root.right, target)
            if left:
                left.append(root)
                return left
            if right:
                right.append(root)
                return right

    def lowestCommonAncestor1(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p == q:
            return p
        if p.left ==  q or p.right == q:
            return p
        if q.left == p or q.right == p:
            return q

        fathers_of_p = self.get_fathers(root, p)
        fathers_of_q = self.get_fathers(root, q)

        length_q = len(fathers_of_q)
        length_p = len(fathers_of_p)
        if length_q < length_p:
            short = fathers_of_q
            long = fathers_of_p
            length_of_short = length_q
            length_of_long = length_p
        else:
            short = fathers_of_p
            long = fathers_of_q
            length_of_short = length_p
            length_of_long = length_q

        # for father in short:
        #     print(father.val, end=" ")
        # print()
        # for father in long:
        #     print(father.val, end=" ")
        # print()
        # short = [3,5]
        # long = [3,5]
        # length_of_long = length_of_short = 2
        for i in range(len(short)):
            print(length_of_short-i-1, length_of_long-1-i)
            if short[length_of_short-i-1] != long[length_of_long-1-i]:
                if length_of_short-i > 0:
                    print(i)
                    return short[length_of_short-i]
                else:
                    break
        return short[0]

    def lowestCommonAncestor2(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p == root or q == root or p.val<root.val<q.val or p.val>root.val>q.val:
            return root
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor2(root.right, p, q)
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor2(root.left, p, q)

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while True:
            if p == root or q == root or p.val<root.val<q.val or p.val>root.val>q.val:
                return root
            if p.val > root.val and q.val > root.val:
                root = root.right
            if p.val < root.val and q.val < root.val:
                root = root.left


def main():
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    p = root.left.right = TreeNode(2)
    print(s.lowestCommonAncestor(root, p, root))


if __name__ == "__main__":
    main()
