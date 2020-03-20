# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import re


def manager(s):
    """
    :type s: str
    :rtype :str
    :param s:
    :return:
    """
    return s.replace(".", "").replace(" ", "_")


def main():
    s = input("please input title:")
    if re.compile(r"^\d").findall(s):
        print("creating the file")
        with open("./"+manager(s)+".py", "w") as f:
            r_str = ""
            with open("./template.title", "r") as rf:
                r_str = rf.read()
            f.write(r_str)
        print("succeeded to creat the file")
        print(manager(s))


if __name__ == "__main__":
    main()
