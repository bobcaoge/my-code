# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        s = set()
        for num in A:
            if num in s:
                return num
            s.add(num)


def main():
    s = Solution()


if __name__ == "__main__":
    main()
