# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = sorted(nums)
        self.length = len(self.nums)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.nums.append(val)
        self.nums.sort()
        self.length += 1
        # print(self.nums)
        return self.nums[-self.k] if 0 < self.k <= self.length else self.nums[-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


def main():
    s = Solution()


if __name__ == "__main__":
    main()
