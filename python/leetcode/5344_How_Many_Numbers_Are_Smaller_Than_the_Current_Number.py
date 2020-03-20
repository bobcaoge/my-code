# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        ret = [0]*len(nums)
        info = sorted([[num, index] for index, num in enumerate(nums)])
        count = 0
        keep = 1<<31
        for i, (num, index) in enumerate(info):
            if num == keep:
                ret[index] = i-count
                count += 1
            else:
                ret[index] = i
                keep = num
                count = 1

        return ret



def main():
    s = Solution()


if __name__ == "__main__":
    main()
