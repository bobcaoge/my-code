# /usr/bin/python3.6
# -*- coding:utf-8 -*-




class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        a = 0
        while True:
            if a*a <= x < (a+1)*(a+1):
                break
            a += 1
        return a


def main():
    s = Solution()
    print(s.mySqrt(4))
    print(s.mySqrt(8))


if __name__ == "__main__":
    main()
