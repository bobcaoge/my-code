# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1 if x == 1 else -1 for x in nums]
        m = {}
        cur_sum = 0
        ret = 0
        for i, num in enumerate(nums):
            cur_sum += num
            if m.get(cur_sum, -1) != -1:
                ret = max(ret, i - m[cur_sum])
            else:
                m[cur_sum] = i
        return ret


def main():
    s = Solution()
    print(s.findMaxLength([0,1,0]))
    print(s.findMaxLength([0,1,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0]))


if __name__ == "__main__":
    main()
