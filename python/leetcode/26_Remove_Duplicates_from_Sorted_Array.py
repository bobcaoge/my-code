# /usr/bin/python3.6
# -*- coding:utf-8 -*-

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_length = len(nums)
        length = 1
        copy_length = 0
        if nums_length <= 1:
            return nums_length
        cur = 0
        while cur<nums_length and length+copy_length<nums_length:
            if cur+1 < nums_length:
                if nums[cur] == nums[cur+1]:
                    buffer = nums[cur]
                    for i in range(cur+1, nums_length-copy_length-1):

                        nums[i] = nums[i+1]
                    nums[nums_length-copy_length-1] = buffer
                    copy_length += 1
                else:
                    cur += 1
                    length += 1
        return length




def main():
    s = Solution()
    a = [0,0,1,1,1,2,2,3,3,4]
    print(s.removeDuplicates(a))

    a = [1,1,2]
    print(s.removeDuplicates(a))

    a = [1,1]
    print(s.removeDuplicates(a))


if __name__ == "__main__":
    main()
