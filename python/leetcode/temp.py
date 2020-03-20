# coding:utf-8
import functools

def cmp(a, b):
    if a[0] > b[0]:
        return 1
    if a[0] < b[0]:
        return -1
    if a[1] <= b[1]:
        return 1
    return -1

def main():
    arr = [[2, 3], [1, 2], [1, 3]]
    arr.sort(key=functools.cmp_to_key(cmp))
    print(arr)

if __name__ == '__main__':
    main()