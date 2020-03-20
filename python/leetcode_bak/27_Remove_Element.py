# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        ret_length = 0
        copy_length = 0
        cur = 0
        length = len(nums)
        while cur < length - copy_length and ret_length + copy_length < length:

            if nums[cur] == val:
                while length-copy_length-1 >= 0 and nums[length-copy_length-1] == val:
                    # print("+",nums[length-copy_length-1])
                    copy_length += 1
                # print(copy_length)
                if length-copy_length-1 <= cur:
                    break
                # print(nums[length-copy_length-1])
                nums[cur] = nums[length-copy_length-1]
                copy_length += 1
                ret_length += 1
            else:
                ret_length += 1
            cur += 1
            # print(ret_length, cur, copy_length)
            # print(nums)
        return ret_length


def main():
    s = Solution()
    nums =[3,2,2,3]
    val = 3
    print(s.removeElement(nums, val))
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print(s.removeElement(nums, val))
    nums = [1]
    val = 1
    print(s.removeElement(nums, val))
    nums = [2, 2, 3, 2]
    val = 2
    print(s.removeElement(nums, val))
    nums = [4, 5]
    val = 5
    print(s.removeElement(nums, val))

if __name__ == "__main__":
    main()
