# /usr/bin/python3.6
# -*- coding:utf-8 -*-

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        i = -1
        j = 0
        x_str = str(x)
        while j - i <= len(x_str):
            if x_str[i] == x_str[j]:
                i -= 1
                j += 1
            else:
                return False
        return True

def main():
    pass


if __name__ == "__main__":
    main()
