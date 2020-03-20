# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        if length <= 1:
            return False
        i = 1
        while i < length:
            if length %i == 0 and s[:i]* int((length/i)) == s:
                return True
        return False



def main():
    s = Solution()


if __name__ == "__main__":
    main()
