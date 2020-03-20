# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class NoneOfQueue(Exception):
    info = "there is no data in queue."


class MyQueue(object):
    def __init__(self):
        self.stack_push = []
        self.stack_pop = []

    def add(self, data):
        self.stack_push.append(data)

    def transport_data_from_stack_push_to_stack_pop(self):
        if self.stack_push.__len__() == 0:
            raise NoneOfQueue
        for _ in range(len(self.stack_push)):
            self.stack_pop.append(self.stack_push.pop())

    def poll(self):
        if len(self.stack_pop) == 0:
            self.transport_data_from_stack_push_to_stack_pop()
        return self.stack_pop.pop()

    def peek(self):
        if len(self.stack_pop) == 0:
            self.transport_data_from_stack_push_to_stack_pop()
        return self.stack_pop[-1]

    def add_many(self, data_list):
        for data in data_list:
            self.add(data)


def main():
    q = MyQueue()
    q.add_many(range(10))
    for _ in range(5):
        print(q.poll(), q.peek())
        # print(q.poll())
        print(q.stack_push, q.stack_pop)
    q.add_many(range(4))
    print(q.stack_push, q.stack_pop)
    for _ in range(9):
        print(q.peek(), q.poll())
        print(q.stack_push, q.stack_pop)


if __name__ == '__main__':
    main()

