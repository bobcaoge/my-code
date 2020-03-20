# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = 0
        ret = 2**32
        cur_sum = 0
        while end < len(nums):
            cur_sum += nums[end]
            if cur_sum >= s:
                ret = min(end-start+1, ret)
                while cur_sum >= s:
                    ret = min(end-start+1, ret)
                    cur_sum -= nums[start]
                    start += 1
            end += 1

        return ret if ret != 2**32 else 0


def main():
    s = Solution()
    print(s.minSubArrayLen(7, [2,3,1,2,4,3]))


if __name__ == "__main__":
    main()
