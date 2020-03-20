# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):

    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ret = [0]*(target+1)
        for i in range(target+1):
            if i in nums:
                ret[i] = 1
            for num in nums:
                if i - num >= 0:
                    ret[i] += ret[i-num]
        return ret[-1]


def main():
    s = Solution()
    print(s.combinationSum4([1,2,3], 4))
    print(s.combinationSum4([4,2,1], 32))
    print(s.combinationSum4([3,33,333],10000))
    print(s.combinationSum4([9],3))


if __name__ == "__main__":
    main()
