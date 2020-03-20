# /usr/bin/python3.6
# -*- coding:utf-8 -*-

class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.stack = [0]*maxSize
        self.length = 0
        self.size = maxSize
        self.adds = [0]*maxSize


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.length < self.size:
            self.stack[self.length] = x
            self.adds[self.length] = 0
            self.length += 1


    def pop(self):
        """
        :rtype: int
        """
        if self.length == 0:
            return -1
        if self.length > 1:
            self.adds[self.length-2] += self.adds[self.length-1]
        self.length -= 1
        ret = self.stack[self.length] + self.adds[self.length]
        return ret




    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        if k > 0:
            self.adds[min(k-1, self.length-1)] += val



def main():
    stack = CustomStack(5)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(8)
    # print(stack.pop())
    stack.increment(3, 2)
    print(stack.adds)
    stack.increment(8, 3)
    print(stack.adds)
    stack.increment(1, 3)
    print(stack.adds)
    print(stack.pop())
    print(stack.adds)
    print(stack.pop())
    print(stack.adds)
    print(stack.pop())
    print(stack.adds)
    print(stack.pop())
    print(stack.adds)
    print(stack.pop())
    print(stack.adds)
    print(stack.stack)
    print(stack.length)
    print(stack.pop())



if __name__ == "__main__":
    main()
