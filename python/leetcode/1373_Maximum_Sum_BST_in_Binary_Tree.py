# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxSumBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ret = 0
        def dfs(r):
            """
            :type r: TreeNode
            :return:
            """
            if r.left and r.right:
                sum_of_left, flag_of_left, max_of_left, min_of_left = dfs(r.left)
                sum_of_right , flag_of_right, max_of_right, min_of_right = dfs(r.right)
                if flag_of_right and flag_of_left and max_of_left < r.val < min_of_right:
                    cur_sum = sum_of_right+sum_of_left+r.val
                    self.ret = max(self.ret, cur_sum)
                    return [cur_sum, True, max_of_right, min_of_left]
            elif r.left is None and r.right:
                sum_of_right , flag_of_right, max_of_right, min_of_right = dfs(r.right)
                if sum_of_right and r.val < min_of_right:
                    cur_sum = sum_of_right+r.val
                    self.ret = max(self.ret, cur_sum)
                    return [cur_sum, True, max_of_right, r.val]
            elif r.right is None and r.left is not None:
                sum_of_left, flag_of_left, max_of_left, min_of_left = dfs(r.left)
                if flag_of_left and max_of_left < r.val:
                    cur_sum = sum_of_left+r.val
                    self.ret = max(self.ret, cur_sum)
                    return [cur_sum, True, r.val, min_of_left]
            else:
                self.ret = max(self.ret, r.val)
                return [r.val, True, r.val, r.val]
            return [0, False, 0, 0]
        dfs(root)
        return self.ret







def main():
    s = Solution()


if __name__ == "__main__":
    main()
