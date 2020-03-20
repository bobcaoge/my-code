# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        if A > B:
            short_num = B
            long_num = A
            short_char = 'b'
            long_char = 'a'
            over = A - B - 1
        else:
            short_num = A
            long_num = B
            short_char = 'a'
            long_char = 'b'
            over = B - A - 1
        ret = ""
        while short_num > 0 or long_num > 0:
            if long_num > 0:
                if over > 0:
                    ret += long_char*2
                    over -= 1
                    long_num -= 2
                else:
                    ret += long_char
                    long_num -= 1
            if short_num > 0:
                ret += short_char
                short_num -= 1
        return ret


    def strWithout3a3b1(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        if A > B:
            long_list = ["aa"] * (A-B-1) + ["a"] * (A - 2*(A-B-1))
            short_list = ["b"] * B
        elif A == B:
            long_list = ["a"] * A
            short_list = ["b"] * B
        else:
            long_list = ["bb"] * (B-A-1) + ["b"] * (B - 2*(B-A-1))
            short_list = ["a"] * A
        ret = ""
        while short_list or long_list:
            if long_list:
                ret += long_list.pop()
            if short_list:
                ret += short_list.pop()
        return ret
def main():
    s = Solution()
    print(s.strWithout3a3b(4,1))


if __name__ == "__main__":
    main()
