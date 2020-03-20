# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join([x for x in s.split(" ") if x != ""][-1::-1])


def main():
    s = Solution()
    print(s.reverseWords("  hello world!  "))


if __name__ == "__main__":
    main()
