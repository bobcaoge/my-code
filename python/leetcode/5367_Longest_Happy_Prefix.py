# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def longestPrefix(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return ''

        def kmp(ss):
            """
            :type ss: str
            :return:
            """
            next_arr = [0]*len(ss)  # next_arr[i]表示 ss[0..i]中必须以s[0]为前缀
                                    # 以s[i]为后缀的最大匹配长度
            cn = 0
            pos = 1
            while pos < len(ss):
                if ss[pos] == ss[cn]:
                    next_arr[pos] = cn+1
                    cn += 1
                    pos += 1
                elif cn > 0:
                    cn = next_arr[cn-1]
                else:
                    next_arr[pos] = 0
                    pos += 1
            return next_arr
        return s[:kmp(s)[-1]]


def main():
    s = Solution()
    print(s.longestPrefix('level'))
    print(s.longestPrefix('bba'))
    print(s.longestPrefix('ababab'))


if __name__ == "__main__":
    main()
