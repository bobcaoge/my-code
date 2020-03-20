# /usr/bin/python3.6
# -*- coding:utf-8 -*-
from data_structure.stack import Stack


def get_min2(s, m):
    if s.is_empty():
        print(m, "m")
        return m
    else:
        # print(len(s), "stack_content")
        buffer = s.pop()
        if buffer < m:
            m = buffer
        # print(m, buffer)
        m = get_min2(s, m)
        s.push(buffer)
        return m


def get_min(stack):
    min_value = stack.pop()

    def get(s, m):
        if s.is_empty():
            # print(m, "m")
            return m
        else:
            # print(len(s), "stack_content")
            buffer = s.pop()
            if buffer < m:
                m = buffer
            # print(m, buffer)
            m = get(s, m)
            s.push(buffer)
            return m

    ret = get(stack, min_value)
    # print(ret, "ret")
    stack.push(min_value)
    return ret


def remove(stack, value):
    if stack.is_empty():
        return
    out = stack.pop()
    if out == value:
        return
    else:
        remove(stack, value)
        stack.push(out)


def sort(stack):
    new_stack = Stack()
    length = stack.length
    print(length)
    for _ in range(length):
        min_value = get_min(stack)
        # print(min_value)
        new_stack.push(min_value)
        remove(stack, min_value)
    print(new_stack)


def main():
    stack = Stack()
    stack.push_all([6, 4, 2, 1, 3, 5, 56, 66])
    print(stack)
    # print(get_min2(stack, stack.peek()))
    # value = get_min(stack)
    # print(value)
    # remove(stack, value)
    # print(stack)
    # for _ in range(6):
    #     min_value = get_min(stack)
    #     print("min_value:{0}".format(min_value))
    #     print("stack:{0}".format(stack))
    #     remove(stack, min_value)
    #     print("stack:{0}".format(stack))
    #     print("====================")
    sort(stack)





if __name__ == '__main__':
    main()
