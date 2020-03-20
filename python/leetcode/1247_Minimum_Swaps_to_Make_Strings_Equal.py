# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def minimumSwap(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        xy = 0
        yx = 0
        for i, c in enumerate(s1):
            if c != s2[i]:
                if c == 'x':
                    xy += 1
                else:
                    yx += 1
        if (xy+yx) % 2 != 0:
            return -1

        return (xy//2 + yx//2) + (yx%2+xy%2)




def main():
    s = Solution()
    print(s.minimumSwap("xx", "yy"))
    print(s.minimumSwap("xy", "yx"))


if __name__ == "__main__":
    main()
