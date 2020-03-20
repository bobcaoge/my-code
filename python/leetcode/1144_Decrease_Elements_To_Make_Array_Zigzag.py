# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def movesToMakeZigzag(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        cur = 0
        # odd greater
        cur += 0 if nums[0] < nums[1] else nums[0]-nums[1]+1
        for i in range(2, len(nums), 2):
            min_num = min(nums[i-1], 1<<31 if i+1 >= len(nums) else nums[i+1])
            if nums[i] >= min_num:
                cur += nums[i] - min_num + 1
        ret = cur
        cur = 0
        # even greater
        for i in range(1, len(nums), 2):
            min_num = min(nums[i-1], 1<<31 if i+1 >= len(nums) else nums[i+1])
            if nums[i] >= min_num:
                cur += nums[i] - min_num + 1
        return min(ret, cur)


def main():
    s = Solution()
    print(s.movesToMakeZigzag([9,6,1,6,2]))
    print(s.movesToMakeZigzag([1,2,3]))
    print(s.movesToMakeZigzag([1, 100,1,1,1,1]))


if __name__ == "__main__":
    main()
