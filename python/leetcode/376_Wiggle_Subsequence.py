# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        ret = 0
        last = 0
        for i in range(1, len(nums)):
            num = nums[i]-nums[i-1]
            if num == 0:
                continue
            if num * last <= 0:
                ret += 1
                last = num

        return ret+1




def main():
    s = Solution()
    print(s.wiggleMaxLength([1,17,5,10,13,13,13,15,10,5,16,8]))
    print(s.wiggleMaxLength([1,7,4,9,2,4]))
    print(s.wiggleMaxLength([0,0]))
    print(s.wiggleMaxLength([0,2,3,4]))
    print(s.wiggleMaxLength([0,2,3,3]))
    print(s.wiggleMaxLength([3,3,3,2,5]))


if __name__ == "__main__":
    main()
