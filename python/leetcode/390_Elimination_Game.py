# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        total = n
        direction = 0 # 0 stand for the direction from left to right
        layer = 0
        while total > 1:
            if direction == 0:
                start += 2**layer
                if total % 2 == 1:
                    end -= 2**layer
            else:
                end -= 2**layer
                if total % 2 == 1:
                    start += 2**layer
            direction = 1-direction
            layer += 1
            total /= 2
        return start


def main():
    s = Solution()
    print(s.lastRemaining(20))
    print(s.lastRemaining(11))
    print(s.lastRemaining(100000000))


if __name__ == "__main__":
    main()
