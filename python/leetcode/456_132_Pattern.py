# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False

        min_num = nums[0]
        before = 1
        after = 1
        while after < len(nums):
            if before == after:
                after += 1
                continue
            if nums[before] <= nums[after]:
                min_num = min(min_num, nums[before])
                before += 1
            else:
                if min_num < nums[after]:
                    return True
                else:
                    after += 1

        after -= 1
        while before < after:
            if min_num < nums[after] and nums[after] < nums[before]:
                return True
            before += 1
            min_num = min(min_num, nums[before])
        return False




def main():
    s = Solution()


if __name__ == "__main__":
    main()
