# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        zeros = [len(x) for x in bin(N)[2:].split("1")[1:-1]]
        if zeros:
            return max(zeros)+1
        return 0


def main():
    s = Solution()


if __name__ == "__main__":
    main()
