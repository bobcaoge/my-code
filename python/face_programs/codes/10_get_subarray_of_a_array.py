# /usr/bin/python3.6
# -*- coding:utf-8 -*-
from data_structure.queue import Queue


def get_num(arr, num):
    if arr is None or len(arr) == 0:
        return

    qmin = Queue()
    qmax = Queue()
    start = 0
    end = 0
    res = 0
    length = len(arr)
    while start < length:
        while end < length:
            while(not qmax.is_empty()) and arr[qmax.peek()] <= arr[end]:
                qmax.poll()
            qmax.add(end)
            while(not qmin.is_empty()) and arr[qmin.peek()] >= arr[end]:
                qmin.poll()
            qmin.add(end)
            if arr[qmax.peek()] - arr[qmin.peek()] > num:
                break
            end += 1
        print(start, end-1)
        res += end - start
        if qmax.peek() == start:
            qmax.poll()
        if qmin.peek() == start:
            qmin.poll()
        start += 1
    return res


def main():
    arr = [1, 4, 2, 5]
    num = 2
    result = get_num(arr, num)
    print(result)


if __name__ == "__main__":
    main()
