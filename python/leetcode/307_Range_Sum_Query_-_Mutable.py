# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.sums = [0]*len(nums)
        self.updated_nums = [0]*len(nums)
        self.all = sum(nums)

    def pre_manage(self):
        last = 0
        for i, num in enumerate(self.nums):
            last += num
            self.sums[i] = last

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        self.updated_nums[i] = val
        self.all += val - self.nums[i]
        self.nums[i] = val

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if j-i > len(self.nums)/2:

            return self.all - sum(self.nums[0:i])-sum(self.nums[j+1:])
        return sum(self.nums[i:j+1])


def main():
    s = NumArray([1,2,3,4,5])
    print(s.sumRange(1, 4))
    print(s.all)
    s.update(2, 0)
    print(s.all)
    print(s.sumRange(1, 4))


if __name__ == "__main__":
    main()
