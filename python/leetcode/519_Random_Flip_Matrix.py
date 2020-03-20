# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import random
import time


class Solution(object):

    def __init__(self, n_rows, n_cols):
        """
        :type n_rows: int
        :type n_cols: int
        """
        self.row = n_rows
        self.column = n_cols
        self.total = n_rows*n_cols-1
        self.record = {}

    def flip(self):
        """
        :rtype: List[int]
        """
        index = random.randint(0, self.total)
        ret = self.record.get(index, index)
        self.record[index] = self.record.get(self.total, self.total)
        self.total -= 1
        return divmod(ret, self.column)


    def reset(self):
        """
        :rtype: None
        """
        self.record = {}
        self.total = self.row*self.column-1


def main():
    s = Solution(10000,10000)
    start = time.time()
    end = time.time()
    print(end-start)


if __name__ == "__main__":
    main()
