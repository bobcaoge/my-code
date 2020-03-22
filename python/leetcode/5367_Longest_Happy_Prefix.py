# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def longestPrefix(self, s):
        """
        :type s: str
        :rtype: str
        """
        def kmp(ss):
            next_arr = [0]*len(ss)
            cn = 0
            pos = 1
            while pos < len(ss):
                if ss[pos] == ss[cn]:
                    next_arr[pos] = cn+1
                    cn += 1
                    pos += 1
                elif cn > 0:
                    cn = next_arr[cn]
                else:
                    next_arr[pos] = 0
                    pos += 1
            return next_arr
        return s[:kmp(s)[-1]]


def main():
    s = Solution()
    print(s.longestPrefix('level'))


if __name__ == "__main__":
    main()
