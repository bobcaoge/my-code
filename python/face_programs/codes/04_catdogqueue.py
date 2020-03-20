# /usr/bin/python3.6
# -*- coding:utf-8 -*-
from data_structure.queue import Queue


class Pet(object):
    def __init__(self, type_of_pet):
        self.type = type_of_pet

    def get_pet_type(self):
        return self.type


class Dog(Pet):
    def __init__(self):
        super(Dog, self).__init__("dog")


class Cat(Pet):
    def __init__(self):
        super(Cat, self).__init__("cat")


class DogCatQueue(object):
    def __init__(self):
        self.content = Queue()
        self.length_of_dog = 0
        self.length_of_cat = 0
        self.length_of_queue = 0

    def add(self, data):
        self.content.add(data)
        if data.get_pet_type == 'cat':
            self.length_of_cat += 1
        elif data.get_pet_type == 'dog':
            self.length_of_dog += 1
        self.length_of_queue += 1

    def poll_all(self):
        return self.poll_all()

    def _poll_what(self, what):
        for _ in range(self.length_of_queue):
            out = self.content.poll()
            if out.get_pet_type == what:
                yield out
            else:
                self.add(out)

    def poll_dog(self):
        self._poll_what('dog')

    def poll_cat(self):
        self._poll_what('cat')

    def is_empty(self):
        return self.length_of_queue == 0

    def is_dog_empty(self):
        return self.length_of_dog == 0

    def is_cat_empty(self):
        return self.length_of_cat == 0


def main():
    data = [x for x in range(4)]
    q = Queue()
    q.add_all(data)
    print(q)


if __name__ == '__main__':
    main()
