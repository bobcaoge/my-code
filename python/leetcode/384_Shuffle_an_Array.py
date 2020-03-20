# /usr/bin/python3.6
# -*- coding:utf-8 -*-
from random import shuffle
from random import randint

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.origin_nums = nums
        self.out = [x for x in nums]

    def my_shuffle(self, nums):
        indexes = [i for i in range(len(self.origin_nums))]
        shuffled = []
        length = len(indexes)
        while indexes:
            index = randint(0, length-1)
            indexes[index], indexes[-1] = indexes[-1], indexes[index]
            shuffled.append(self.origin_nums[indexes.pop()])
            length -= 1
        self.out = shuffled

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.out = [x for x in self.origin_nums]
        return self.out

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        self.my_shuffle(self.out)
        return self.out



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()


def main():
    obj = Solution([1,2,3])
    param_1 = obj.reset()
    param_2 = obj.shuffle()
    # print(param_1, param_2)
    for i in range(20):
        print("reset: ", obj.reset())
        print("shuffle: ", obj.shuffle())



if __name__ == "__main__":
    main()
