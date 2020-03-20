# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import re


def manage_str(s):
    pattern = r" |#.*"
    pattern = re.compile(pattern)
    for item in set(pattern.findall(s)):
        s = s.replace(item, "")
    return s


def get(filename):
    line_list = []
    with open(filename, "r") as f:
        for line in f.readlines():
            l = manage_str(line)
            if len(l) > 0:
                line_list.append(l)
        return line_list


src_filename = "NLP_p.py"
dest_filename = "test_nlp.py"

src_line_list = get(src_filename)
dest_line_list = get(dest_filename)

for index, (x, y) in enumerate(zip(src_line_list, dest_line_list)):
    # print(x, y)
    if x != y:
        print("src:" + x + "\n" + "dest:" + y)




