#! /usr/bin/python3.6
#-*- coding:utf-8 -*-
def manager(length_of_river, arr):
    res = lo = hi = 0
    i = 0
    arr.sort()
    while i < len(arr):
        lo = hi
        for k in range(i, len(arr)):
            if arr[k][0] <= lo:
                hi = max(hi, arr[k][1])
            else:
                i = k
                break

        res += 1
        if lo == hi:
            return -1
        if hi >= length_of_river:
            break
    return res

def main():
    n, L =(int(x) for x in input().split(' '))
    arr = []
    for i in range(n):
        arr.append([int(x) for x in input().split(' ')])
    print(manager(L, arr))


if __name__ == "__main__":
    main()