# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        if len(palindrome) == 1:
                return ''
        for i in range(len(palindrome)//2):
            c = palindrome[i]
            if c != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]
        return palindrome[:-1]+'b'


def main():
    s = Solution()
    print(s.breakPalindrome('abccba'))
    print(s.breakPalindrome('aa'))


if __name__ == "__main__":
    main()
