# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import collections


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 0:
            flag = True
            nums.sort()
            ret = 0
            for i in range(len(nums)-1):
                if nums[i] == nums[i+1] and flag:
                    ret += 1
                    flag = False
                if nums[i] != nums[i+1]:
                    flag = True
            return ret
        nums = list(set(nums))
        nums.sort()
        ret = 0
        diffs = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]
        print(diffs)
        for index, diff in enumerate(diffs):
            sum_num = diff
            if sum_num == k:
                ret += 1
            for diff2 in diffs[index + 1:]:
                sum_num += diff2
                if sum_num == k:
                    ret += 1
                elif sum_num > k:
                    break

        return ret

    def findPairs1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 0:
            return sum(x > 1 for x in collections.Counter(nums).values())
        elif k > 0:
            return len(set(nums) & set(n + k for n in nums))
        else:
            return 0


def main():
    s = Solution()
    print(s.findPairs([1,2,3,4,5], 1))
    print(s.findPairs([3,1,4,1,5], 2))
    print(s.findPairs([1,2,3,4,5], 3))
    print(s.findPairs([1,1,1,1,1], 0))


if __name__ == "__main__":
    main()
