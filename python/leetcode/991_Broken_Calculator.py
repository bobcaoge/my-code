# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        ret = 0
        while X < Y:
            if Y % 2 == 0:
                Y //= 2
                ret += 1
            else:
                Y = (Y+1)//2
                ret += 2
        return ret + X - Y


def main():
    s = Solution()
    print(s.brokenCalc(2,3))
    print(s.brokenCalc(3,10))
    print(s.brokenCalc(1024, 1))
    print(s.brokenCalc(999999,1000001))


if __name__ == "__main__":
    main()
