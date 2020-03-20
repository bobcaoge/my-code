# /usr/bin/python3.6
# -*- coding:utf-8 -*-
class Solution(object):
    def reachNumber(self, target):
        target = abs(target)
        k = 0
        while target > 0:
            k += 1
            target -= k

        return k if target % 2 == 0 else k + 1 + k%2


def main():
    s = Solution()


if __name__ == "__main__":
    main()
