# /usr/bin/python3.6
# -*- coding:utf-8 -*-

class NumArray:

    def __init__(self, nums: 'List[int]'):
        self.nums = nums
        self.sum_list = self.get_sums(nums)
        self.length = len(nums)

    def get_sums(self, nums):
        sum_list = []
        buffer = 0
        for num in nums:
            buffer += num
            sum_list.append(buffer)
        return sum_list

    def sumRange(self, i: 'int', j: 'int') -> 'int':
        if i <= j:
            if i > 0:
                return self.sum_list[j] - self.sum_list[i-1]
            else:
                return self.sum_list[j]


def main():
    # s = Solution()
    pass


if __name__ == "__main__":
    main()
