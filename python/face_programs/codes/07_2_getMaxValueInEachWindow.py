# /usr/bin/python3.6
# -*- coding:utf-8 -*-
from data_structure.queue import Queue


def get_max_values_of_list(data_list, window_length):
    q = Queue()
    res = []
    for index, data in enumerate(data_list):
        put_queue(q, index, data_list)
        if q.peek() == index - window_length:
            q.poll()

        if index >= window_length-1:
            res.append(data_list[q.peek()])
    return res


def put_queue(q, index, data_list):
    while (not q.is_empty()) and data_list[q.peek_left()] < data_list[index]:
        q.poll_left()
    q.add(index)


def main():
    data_list = [4, 3, 5, 4, 3, 3, 6, 7]
    ret = get_max_values_of_list(data_list, window_length=3)
    print(ret)


if __name__ == '__main__':
    main()
