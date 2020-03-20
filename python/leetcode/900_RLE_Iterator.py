# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class RLEIterator(object):

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.sequence = A
        self.cursor = 0
        self.length = len(A)


    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        while self.cursor < self.length and self.sequence[self.cursor] < n:
            n -= self.sequence[self.cursor]
            self.cursor += 2
        if self.cursor < self.length:
            self.sequence[self.cursor] -= n
            return self.sequence[self.cursor+1]
        else:
            return -1


def main():
    pass


if __name__ == "__main__":
    main()
