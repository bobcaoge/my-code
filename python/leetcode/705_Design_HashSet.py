# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        if key not in self.nums:
            self.nums.append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        if key in self.nums:
            self.nums.remove(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        if key in self.nums:
            return True
        return False


def main():
    s = Solution()


if __name__ == "__main__":
    main()
