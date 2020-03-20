#! /usr/bin/python3.6
#-*- coding:utf-8 -*-

def manager(arr):
    length = len(arr)
    dp1 = [0]*length
    stack = []
    for i, height in enumerate(arr):
        while stack and arr[stack[-1]]<=height:
            stack.pop()
        stack.append(i)
        dp1[i] = len(stack)
    dp2 = [0]*length
    stack = []
    for i in range(length-1, -1, -1):
        while stack and arr[stack[-1]]<=arr[i]:
            stack.pop()
        stack.append(i)
        dp2[i] = len(stack)
    # print(dp1)
    # print(dp2)
    ret = [0]*length
    for i in range(length):
        ret[i] += (0 if i-1 < 0 else dp1[i-1]) + (0 if i+1 >= length else dp2[i+1])+1
    return ret


def main():
    num = input()
    arr = [int(x) for x in input().split(' ')]
    for num in manager(arr):
        print(num, end=' ')


if __name__ == "__main__":
    main()