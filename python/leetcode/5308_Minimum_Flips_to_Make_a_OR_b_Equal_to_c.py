# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        ret = 0
        while c > 0 or a > 0 or b > 0:

            last_bit_of_a = a & 1
            last_bit_of_b = b & 1
            last_bit_of_c = c & 1
            if last_bit_of_c == 0:
                ret += last_bit_of_a+last_bit_of_b
            if last_bit_of_c == 1 and last_bit_of_a == 0 and last_bit_of_b == 0:
                ret += 1
            a >>= 1
            b >>= 1
            c >>= 1
        return ret


def main():
    s = Solution()
    print(s.minFlips(8,3,5))


if __name__ == "__main__":
    main()
