# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ret = m
        diff = n-m
        i = 0
        last = 0
        x = 1
        while m != 0:
            if m % 2 == 1:
                last += x
                if x*2 - last <= diff:
                    ret -= x
            m >>= 1
            i += 1
            x *= 2
        return ret
    def rangeBitwiseAnd1(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ret = m
        buff = bin(ret)[-1::-1][:-2]
        i = 0
        last = 0
        while i < len(buff):
            if buff[i] == "1":
                x = 2**i
                last += x
                if x*2 - last <= n - m:
                    ret -= x
            i += 1
        return ret



def main():
    s = Solution()
    print(s.rangeBitwiseAnd(5,7))
    print(s.rangeBitwiseAnd(5,8))
    print(s.rangeBitwiseAnd(3,4))
    print(s.rangeBitwiseAnd(600000000, 2147483645))
    print(s.rangeBitwiseAnd(3, 3))


if __name__ == "__main__":
    main()
