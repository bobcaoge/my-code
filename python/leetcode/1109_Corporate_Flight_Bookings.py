# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        ret = [0]*n
        for start, end, num in bookings:
            ret[start-1] += num
            if end < n:
                ret[end] -= num
        for i in range(1, n):
            ret[i] += ret[i-1]
        return ret


def main():
    s = Solution()
    print(s.corpFlightBookings(bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5))


if __name__ == "__main__":
    main()
