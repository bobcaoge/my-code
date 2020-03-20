# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import time


class FooBar(object):
    def __init__(self, n):
        self.n = n
        self.flag = False


    def foo(self, printFoo):
        """
        :type printFoo: method
        :rtype: void
        """
        for i in range(self.n):

            while self.flag:
                time.sleep(0.001)
            self.flag = not self.flag
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()


    def bar(self, printBar):
        """
        :type printBar: method
        :rtype: void
        """
        for i in range(self.n):
            while not self.flag:
                time.sleep(0.001)
            self.flag = not self.flag
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()


def main():
    pass


if __name__ == "__main__":
    main()
