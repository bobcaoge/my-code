# /usr/bin/python3.6
# -*- coding:utf-8 -*-

class Solution(object):
    def twoSum(self, nums, target):
        for indexi, numi in enumerate(nums):
            for indexj, numj in enumerate(nums):
                if indexi != indexj and numi + numj == target:
                    return [indexi, indexj]


def main():
    s = Solution()
    print(s.twoSum([1,2,3,4,5,6,7], 8))
    pass


if __name__ == "__main__":
    main()
