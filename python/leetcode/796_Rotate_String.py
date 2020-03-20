# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """

        return len(A) == len(B) and (A+A).find(B) != -1


def main():
    s = Solution()
    print(s.rotateString("abcde", ""))


if __name__ == "__main__":
    main()
