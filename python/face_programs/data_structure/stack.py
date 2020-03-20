# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class NoneOfStack(Exception):
    info = "stack is empty"


class Stack(object):
    def __init__(self):
        self._stack = []
        self.length = 0

    def pop(self):
        try:
            self.length -= 1
            return self._stack.pop()

        except NoneOfStack:
            raise NoneOfStack()

    def push(self, value):
        self._stack.append(value)
        self.length += 1

    def push_all(self, values):
        for value in values:
            self.push(value)

    def is_empty(self):
        return self.length == 0

    def __str__(self):
        return self._stack.__str__()

    def __len__(self):
        return len(self._stack)

    def peek(self):
        return self._stack[-1]

    def size(self):
        return self.length


def main():
    stack = Stack()
    stack.push_all([x for x in range(10)])
    print(stack)
    length = stack.length
    for _ in range(length):
        print(stack.pop(), stack.length)
        print(stack)
        print(stack.is_empty())


if __name__ == '__main__':
    main()