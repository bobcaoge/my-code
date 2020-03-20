# /usr/bin/python3.6
# -*- coding:utf-8 -*-


def main():
    n = input()
    n = int(n)
    ans = 0
    arr = input()
    arr = arr.split(" ")
    arr = [int(arr[i]) for i in range(n)]
    s = set()
    for i in range(1, n):
           if arr[i] < arr[i-1]:
               ans += 1
               s.add(i)
               s.add(i-1)
    flag = True
    for i in range(n):
        if i not in s and flag:
            ans += 1
            flag = False
        else:
            flag = True


    temp = ans
    ans = 0
    s = set()
    for i in range(1, n):
           if arr[i] > arr[i-1] :
               ans += 1
               s.add(i)
               s.add(i-1)
    flag = True
    for i in range(n):
        if i not in s and flag:
            ans += 1
            flag = False
        else:
            flag = True


    print(min(ans, temp))


if __name__ == "__main__":
    main()
