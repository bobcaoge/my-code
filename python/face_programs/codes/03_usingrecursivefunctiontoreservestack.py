# /usr/bin/python3.6
# -*- coding:utf-8 -*-


def get(stack):
    result = stack.pop()
    if stack.__len__() == 0:
        print("result:"+str(result))
        return result
    else:
        last = get(stack)
        stack.append(result)
        return last


def reverse_stack(stack):
    if stack.__len__() == 0:
        return
    a = get(stack)
    reverse_stack(stack)
    stack.append(a)


def main():
    stack = [x for x in range(10)]
    print(stack)
    reverse_stack(stack)
    print(stack)


if __name__ == '__main__':
    main()
