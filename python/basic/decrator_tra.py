#! /usr/bin/python3.6
# -*- coding:utf-8 -*-
from functools import wraps


def dec(func):
    @wraps(func)
    def wrapper():
        print("start wrapping")
        func()
        print("end wrapping")
    return wrapper


@dec
def login(username="bob", password="passwd"):
    print("welcome {0} to login".format(username))


def main():
    login()
    print(login.__name__)


if __name__ == "__main__":
    main()