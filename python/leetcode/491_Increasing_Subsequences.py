# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = set()
        ret.add(())
        for i in range(len(nums)):
            buff = set()
            for arr in ret:
                if not arr:
                    buff.add((nums[i],))
                else:
                    arr_list = list(arr)
                    if arr_list[-1] <= nums[i]:
                        buff.add(tuple(arr_list+[nums[i]]))
                buff.add(arr)
            ret = buff
        return [list(arr) for arr in ret if len(arr)>1]


def main():
    s = Solution()
    print(s.findSubsequences([4,6,7,7]))


if __name__ == "__main__":
    main()
