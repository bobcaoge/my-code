# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        start = 0
        end = 0
        ret = []
        for i in range(1, len(nums)):
            if nums[i] - nums[end] == 1:
                end = i
            else:
                if start == end:
                    ret.append(str(nums[start]))
                else:
                    ret.append("{0}->{1}".format(nums[start],nums[end]))
                start = end = i
        if start == end:
            ret.append(str(nums[start]))
        else:
            ret.append("{0}->{1}".format(nums[start],nums[end]))
        return ret


def main():
    s = Solution()
    print(s.summaryRanges([0,1,2,4,5,7]))
    print(s.summaryRanges([0,2,3,4,6,8,9]))


if __name__ == "__main__":
    main()
