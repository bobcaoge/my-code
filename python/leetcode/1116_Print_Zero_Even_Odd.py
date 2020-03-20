# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import threading
from threading import Condition


class ZeroEvenOdd(object):
    def __init__(self, n):
        self.n = n
        self.zero_condition = 0
        self.other_condition = 0
        self.condition = Condition()


    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(self.n):
            with self.condition:
                self.condition.wait_for(lambda :self.zero_condition == self.other_condition)
                printNumber(0)
                self.zero_condition += 1
                self.condition.notify(2)


    def even(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(self.n//2):
            with self.condition:
                self.condition.wait_for(lambda: self.zero_condition > self.other_condition and self.other_condition % 2 == 1)
                self.other_condition += 1
                printNumber(self.other_condition)
                self.condition.notify(2)


    def odd(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(self.n//2+ (self.n% 2)):
            with self.condition:
                self.condition.wait_for(lambda: self.zero_condition > self.other_condition and self.other_condition % 2 == 0)
                self.other_condition += 1
                printNumber(self.other_condition)
                self.condition.notify(2)




def main():
    s = ZeroEvenOdd(10)


if __name__ == "__main__":
    main()
