# /usr/bin/python3.6
# -*- coding:utf-8 -*-
from random import choice

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.place = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.place:
            self.data.append(val)
            self.place[val] = len(self.data)-1
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.place:
            place = self.place[val]
            self.place[self.data[-1]] = place
            self.data[place], self.data[-1] = self.data[-1], self.data[place]
            self.data.pop()
            self.place.pop(val)
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return choice(self.data)





# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


def main():
    s = Solution()


if __name__ == "__main__":
    main()
