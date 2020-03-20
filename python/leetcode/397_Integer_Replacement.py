# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):

    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        step = 0
        while n != 1:
            # print(n)
            if n % 2 == 0:
                n /= 2
            else:
                return min(self.integerReplacement(n+1), self.integerReplacement(n-1))+step+1
            step += 1
        return step


def main():
    s = Solution()
    print(s.integerReplacement(999))
    print(s.integerReplacement(999999999))


if __name__ == "__main__":
    main()
