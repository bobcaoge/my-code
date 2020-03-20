# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):

    def cycle(self, nums, length):
        buffer = nums[-1]
        for i in range(length-1):
            nums[length-1-i] = nums[length-2-i]
        nums[0] = buffer

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k%length
        for i in range(k):
            self.cycle(nums, length)

        print(nums)


    def rotate1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        if k == 0:
            return
        front = nums[length-k:]
        tail = nums[:length - k]
        print(front, tail)
        for i in range(len(front)):
            nums[i] = front[i]
        for i in range(len(tail)):
            nums[i+len(front)] = tail[i]
        print(nums)






def main():
    s = Solution()

    s.rotate([1,2,3,4,5,6,7], 3)
    s.rotate([1,2,3,4,5,6], 1)



if __name__ == "__main__":
    main()
