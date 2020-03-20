# /usr/bin/python3.6
# -*- coding:utf-8 -*-
from data_structure.stack import Stack


def sort_stack(stack):
    if stack.is_empty():
        return stack
    new_stack = Stack()
    while not stack.is_empty():
        cur = stack.pop()
        if new_stack.is_empty():
            new_stack.push(cur)
        else:
            if cur <= new_stack.peek():
                new_stack.push(cur)
            else:
                while cur > new_stack.peek():
                    stack.push(new_stack.pop())
                    if new_stack.is_empty():
                        new_stack.push(cur)
                        break
                else:
                    new_stack.push(cur)
    return new_stack


def sort_stack2(stack):
    if stack.is_empty():
        return stack
    new_stack = Stack()
    while not stack.is_empty():
        cur = stack.pop()
        while (not new_stack.is_empty()) and (new_stack.peek() > cur):
            stack.push(new_stack.pop())
        new_stack.push(cur)
    return new_stack


def main():
    stack = Stack()
    stack.push_all([2, 6, 1, 87, 2, 33])
    new_stack = sort_stack2(stack)
    print(new_stack)


if __name__ == '__main__':
    main()
