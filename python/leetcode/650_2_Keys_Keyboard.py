# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def minSteps(self, n):
        ans = 0
        d = 2
        while n > 1:
            while n % d == 0:
                ans += d
                n /= d
            d += 1
        return ans




def main():
    s = Solution()
    print(s.minSteps(3))


if __name__ == "__main__":
    main()
