# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.ite = iterator
        self.flag = False
        self.ret = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.flag:
            return self.ret
        self.flag = True
        self.ret = self.ite.next()
        return self.ret


    def next(self):
        """
        :rtype: int
        """
        if self.flag:
            self.flag = False
            return self.ret
        else:
            return self.ite.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.flag:
            return True
        else:
            return self.ite.hasNext()


def main():
    pass


if __name__ == "__main__":
    main()
