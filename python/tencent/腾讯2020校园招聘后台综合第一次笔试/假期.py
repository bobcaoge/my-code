#! /usr/bin/python3.6
#-*- coding:utf-8 -*-
import heapq

def manager(corporate, fitness):
    length = len(corporate)
    heap = [[0, -1, 0]] # 最少休息天数为0, 第0天 当天休息，
    visited = set()
    while heap:
        num, cur_day, state = heapq.heappop(heap)
        if (cur_day, state) in visited:
            continue
        visited.add((cur_day, state))
        if cur_day == length-1:
            return num
        if state == 0:
            if corporate[cur_day+1] == 1:
                heapq.heappush(heap, [num, cur_day+1, 1])
            if fitness[cur_day+1] == 1:
                heapq.heappush(heap, [num, cur_day+1, 2])
            heapq.heappush(heap, [num+1, cur_day+1, 0])  #待定
        elif state == 1:
            if fitness[cur_day+1] == 1:
                heapq.heappush(heap, [num, cur_day+1, 2])
            heapq.heappush(heap, [num+1, cur_day+1, 0])
        elif state == 2:
            if corporate[cur_day+1] == 1:
                heapq.heappush(heap, [num, cur_day+1, 1])
            heapq.heappush(heap, [num+1, cur_day+1, 0])


def main():
    num = input()
    corporate = [int(x) for x in input().split(' ')]
    fitness = [int(x) for x in input().split(' ')]
    print(manager(corporate, fitness))


if __name__ == "__main__":
    main()