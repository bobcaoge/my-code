# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def shortestPalindrome(self, s):
        """
        KMP algorithm
        :type s: str
        :rtype: str
        """
        record = s
        s = s + "#" + s[::-1]
        next_arr = [0]*(len(s)+1)
        next_arr[0] = -1
        pos = 2
        cn = 0
        while pos < len(s)+1:
            if s[pos-1] == s[cn]:
                next_arr[pos] = cn+1
                pos += 1
                cn += 1
            elif next_arr[cn] == -1:
                pos += 1
            else:
                cn = next_arr[cn]
        return record[next_arr[-1]:][::-1] + record


def main():
    s = Solution()
    print(s.shortestPalindrome("aba"))
    print(s.shortestPalindrome("abac"))
    print(s.shortestPalindrome("abcd"))
    print(s.shortestPalindrome('a'))
    print(s.shortestPalindrome('aa'))
    print(s.shortestPalindrome("aacecaa"))
    print(s.shortestPalindrome("aacecaab"))


if __name__ == "__main__":
    main()
