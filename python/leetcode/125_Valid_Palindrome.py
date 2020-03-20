# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import re


class Solution(object):
    pattern = re.compile(r"([a-zA-Z\d])")
    def manage(self, s):
        """
        :type s: str
        :param s:
        :return:
        """
        if 'a' <= s <= 'z':
            return s
        elif 'A' <= s <= 'Z':
            return s.lower()
        elif '0' <= s <= '9':
            return s
        else:
            return ""

    def isPalindrome1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = 0
        end = len(s) - 1
        while start < end:
            s_start = self.manage(s[start])
            s_end = self.manage(s[end])
            if s_end and s_start:
                if s_end == s_start:
                    start += 1
                    end -= 1
                else:
                    return False
            elif s_start:
                end -= 1
            elif s_end:
                start += 1
            else:
                start += 1
                end -= 1
        return True

    def isPalindrome(self, s):
        result = "".join(self.pattern.findall(s)).lower()
        print(result)
        start = 0
        end = len(result) - 1
        while start < end:
            if result[start] != result[end]:
                return False
            start += 1
            end -= 1

        return True


def main():
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))
    print(s.isPalindrome("race a car"))
    print(s.isPalindrome("0P"))


if __name__ == "__main__":
    main()
