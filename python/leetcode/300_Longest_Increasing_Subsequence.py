# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        ret = [1]*len(nums)
        for i, num in enumerate(nums):
            if i == 0:
                ret[i] = 1
            else:
                for j in range(i):
                    if nums[j] < num:
                        ret[i] = max(ret[j]+1, ret[i])
        print(ret)
        return max(ret)


def main():
    s = Solution()
    print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))


if __name__ == "__main__":
    main()
