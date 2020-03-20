# /usr/bin/python3.6
# -*- coding:utf-8 -*-

class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        def enough(num):
            return sum([min(num//i, n) for i in range(1, m+1)]) >= k

        start = 1
        end = m*n
        while start < end:
            mid = (start + end)//2
            if enough(mid):
                end = mid
            else:
                start = mid + 1
        return end






def main():
    s = Solution()
    print(s.findKthNumber(30000, 30000, 30000000))


if __name__ == "__main__":
    main()
