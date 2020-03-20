# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Queue(object):
    def __init__(self):
        self._content = []
        self.length = 0

    def is_empty(self):
        """
        :return:
        """
        return self._content.__len__() == 0

    def add(self, data):
        """
        数据入队
        :param data: 要入队的数据
        :return:
        """
        self._content.insert(0, data)
        self.length += 1

    def poll(self):
        """
        出队
        :return:
        """
        self.length -= 1
        return self._content.pop()

    def peek(self):
        """
        获取队列出队口的数据
        :return:
        """
        return self._content[-1]

    def add_all(self, data_list):
        """
        将列表中的数据依次入队
        :param data_list: 要入队的数据组成的列表
        :return:
        """
        for data in data_list:
            self.add(data)

    def poll_all(self):
        """
        依次出队所有数据
        :return:
        """
        for _ in range(self.length):
            yield self._content.pop()

    def __str__(self):
        return self._content.__str__()

    def poll_left(self):
        """
        出队最左边的数据
        :return:
        """
        return self._content.pop(0)

    def peek_left(self):
        """
        获取队列最左边的数据
        :return:
        """
        return self._content[0]


def main():
    q = Queue()
    q.add_all([x for x in range(10)])
    print(q)
    # for i in range(q.length):
    #     print(q.poll())
    #     print(q)
    result = q.poll_all()
    for out in result:
        print(out)



if __name__ == '__main__':
    main()

