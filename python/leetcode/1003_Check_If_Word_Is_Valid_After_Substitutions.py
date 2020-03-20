# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def isValid(self, S):
        """
        :type S: str
        :rtype: bool
        """
        old = S
        S = S.replace("abc", "")
        while old != S and len(S) > 3:
            old = S
            S = S.replace("abc", "")

        if S in {"", "abc"}:
            return True
        return False


def main():
    s = Solution()


if __name__ == "__main__":
    main()
