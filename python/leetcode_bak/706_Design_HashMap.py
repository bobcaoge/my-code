# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        if len(self.nums) == 0:
            self.nums.append([key, value])
        else:
            flag = False
            for num in self.nums:
                if num[0] == key:
                    num[1] = value
                    flag = True
                    break
            if not flag:
                self.nums.append([key, value])

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        for info in self.nums:
            if info[0] == key:
                return info[1]
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        for info in self.nums:
            if info[0] == key:
                self.nums.remove(info)
                break


def main():
    s = Solution()


if __name__ == "__main__":
    main()
