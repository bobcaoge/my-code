# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        voyage = voyage[::-1]
        ret = []

        def traverse(r):
            if r:
                if r.val != voyage[-1]:
                    return
                voyage.pop()
                if not r.left and not r.right:
                    return
                if r.left and r.left.val == voyage[-1]:
                    traverse(r.left)
                    traverse(r.right)
                elif r.right and r.right.val == voyage[-1]:
                    if r.left:
                        ret.append(r.val)
                    traverse(r.right)
                    traverse(r.left)

        traverse(root)
        return [-1] if voyage else ret








def main():
    s = Solution()


if __name__ == "__main__":
    main()
