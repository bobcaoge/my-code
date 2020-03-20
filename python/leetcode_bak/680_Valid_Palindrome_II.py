# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def test(self, s):
        length = len(s)
        start = 0
        end = length - 1
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        start = 0
        end = length - 1
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                break
        if start == end:
            return True
        return self.test(s[start:end]) or self.test(s[start+1:end+1])


def main():
    s = Solution()
    print(s.validPalindrome("ebcbbececabbacecbbcbe"))


if __name__ == "__main__":
    main()
