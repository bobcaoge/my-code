# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = [0] * 128
        for c in s:
            m[ord(c)] += 1

        odd_flag = False
        ret = 0
        for i in m:
            if i % 2 == 0:
                ret += i
            else:
                if i > 1:
                    ret += i - 1
                odd_flag = True
        return ret+1 if odd_flag else ret



def main():
    s = Solution()


if __name__ == "__main__":
    main()
