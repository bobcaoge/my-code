# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        diff = 0
        for num in nums:
            diff ^= num
        diff &= -diff
        ret = [0, 0]
        for num in nums:
            if diff & num == 0:
                ret[0] ^= num
            else:
                ret[1] ^= num
        return ret


def main():
    s = Solution()


if __name__ == "__main__":
    main()
