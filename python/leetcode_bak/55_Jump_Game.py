# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length_of_nums = len(nums)
        i = length_of_nums-1
        flag = True
        length = 0

        while i >= 0:
            if nums[i] == 0:
                if flag:
                    if i == length_of_nums-1:
                        length = 0
                    else:
                        length = 1
                    flag = False
                else:
                    length += 1
                i-=1
                continue
            if flag is False:
                if nums[i] > length:
                    flag = True
                length += 1
            i -= 1
        if length_of_nums == 1 and not flag:
            return True

        return flag


def main():
    s = Solution()
    print(s.canJump([2,3,1,1,4]))
    print(s.canJump([3,2,1,0,4]))
    print(s.canJump([0,2,1,0,4]))
    print(s.canJump([0]))
    print(s.canJump([0,0]))
    print(s.canJump([9,0,0,0,0]))
    print(s.canJump([4,0,0,0,0]))
    print(s.canJump([3,0,0,1,0]))
    print(s.canJump([0,9,0,1,0]))


if __name__ == "__main__":
    main()
