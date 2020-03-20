# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def buffer(self, nums, start, end):
        record = 0
        for mid in range(start, end + 1):
            lefts = self.buffer(nums, start, mid - 1)
            rights = self.buffer(nums, mid + 1, end)
            if lefts and rights:
                record += lefts*rights
            elif lefts:
                record += lefts
            elif rights:
                record += rights
            else:
                record += 1
        return record

    def numTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        ret = [0]*(n+1)
        ret[0] = ret[1] = 1
        for i in range(2, n+1):
            for j in range(i):
                ret[i] += ret[j]*ret[i-j-1]
        return ret[n]


def main():
    s = Solution()
    print(s.numTrees(3))
    print(s.numTrees(4))
    print(s.numTrees(5))
    print(s.numTrees(6))


if __name__ == "__main__":
    main()
