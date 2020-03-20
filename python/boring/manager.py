# coding:utf-8
import re


def manage_string(s):
    s = re.sub(re.compile(r"[\r\n|\r|\n|\n\r]"), "", s)
    return s


if __name__ == "__main__":
    with open("./result.txt", "w") as ff:
        with open("./temp.txt", "r") as f:
            lines = f.readlines()
            # print(lines)
            for line in lines:
                # print(line, line.strip())
                if line.strip() != "":
                    ff.write(manage_string(line))
                else:
                    ff.write("\n\r")

