# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = ""
        i = 0
        m = {}
        for j in range(1, 10):
            m[str(j)] = chr(j-1+ord('a'))
        for j in range(10, 27):
            m['{0}#'.format(j)] = chr(j-10+ord('j'))
        # print(m)
        while i < len(s):
            if i + 2 < len(s) and s[i+2] == '#':
                ret += m[s[i:i+3]]
                i += 3
            else:
                ret += m[s[i]]
                i += 1
        return ret


def main():
    s = Solution()
    print(s.freqAlphabets("10#11#12"))
    print(s.freqAlphabets("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"))


if __name__ == "__main__":
    main()
