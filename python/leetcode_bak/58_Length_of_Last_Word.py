# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 1:
            if s[0] != " ":
                return 1
            else:
                return 0
        ret_length = 0
        index = 0
        while index < length:
            # print(ret_length)
            if s[-(index+1)] != " ":
                ret_length += 1
            else:
                if ret_length > 0:
                    break
            index += 1
        return ret_length


def main():
    s = Solution()
    print(s.lengthOfLastWord("a  "))
    print(s.lengthOfLastWord("hello world"))


if __name__ == "__main__":
    main()
