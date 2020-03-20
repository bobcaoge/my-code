# /usr/bin/python3.6
# -*- coding:utf-8 -*-


def inverse(x):
    flag = False
    ret = 0

    if x<0:
        flag = True
        x = -x
    while x != 0:
        ret = ret*10 + x%10
        x = int(x/10)
    if flag:
        ret = -ret
    if ret < -2147483648 or ret > 2147483647:
        return 0
    return ret
def main():
    print(inverse(1534236469))


if __name__ == "__main__":
    main()
