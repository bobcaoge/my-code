# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def numberOfSteps (self, num):
        """
        :type num: int
        :rtype: int
        """
        ret = 0
        while num != 0:
            if num % 2 == 1:
                num -= 1
            else:
                num /= 2
            ret += 1
        return ret


def main():
    s = Solution()
    print(s.numberOfSteps(14))


if __name__ == "__main__":
    main()
