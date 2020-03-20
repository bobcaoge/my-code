# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        def dfs(i, direction):
            """
            :param i:
            :param old:
            :param direction: 搜索的方向 True 代表 forward ，False 代表 backward
            :return:
            """

            if nums[i] == -2000:
                return True
            if nums[i] == 2000:
                return False
            if direction != (nums[i] > 0):
                return False
            n = (nums[i] + i+len(nums)) % len(nums)
            nums[i] = -2000
            ret = False
            if n != i:
                ret = dfs(n, direction)

            nums[i] = 2000
            return ret
        for i in range(len(nums)):
            if dfs(i, nums[i]>0):
                return True
        return False


def main():
    s = Solution()
    print(s.circularArrayLoop([2,-1,1,2,2]))
    print(s.circularArrayLoop([-2,1,-1,-2,-2]))
    print(s.circularArrayLoop([-1, 2]))
    print(s.circularArrayLoop([2,-1,1,-2,-2])) # False


if __name__ == "__main__":
    main()
