# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import random


class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.weights_nums = self.get_nums(w)

    def get_nums(self, weights):
        old = 1
        nums = [1]
        for weight in weights:
            old += weight
            nums.append(old)
        return nums

    def pickIndex(self):
        """
        :rtype: int
        """
        weight = random.randint(1, self.weights_nums[-1]-1)
        # print(weight)
        return self.get_index(weight)

    def get_index(self, weight):
        start = 0
        end = len(self.weights_nums)-1
        mid = (start+end)/2
        while start < end:
            if self.weights_nums[mid] == weight:
                return mid
            elif self.weights_nums[mid] > weight:
                end = mid - 1
            else:
                if mid + 1 < len(self.weights_nums):
                    if self.weights_nums[mid + 1] > weight:
                        return mid
                    else:
                        start = mid + 1
            mid = (start+end)/2
        return start


def test():
    s = Solution([1,2,3,4])
    for i in range(1, s.weights_nums[-1]):
        print(i, s.get_index(i))


def main():
    s = Solution([1,2,3,4])
    print(s.weights_nums)
    record = [0]*4
    for i in range(100000):
        # print(s.pickIndex())
        record[s.pickIndex()] += 1

    sum_ = sum(record)
    for i, num in enumerate(record):
        print(i, num/10000.0)


if __name__ == "__main__":
    main()
    # test()
