# /usr/bin/python3.6
# -*- coding:utf-8 -*-

class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return 0
        m = [0]*11
        m[1] = 1
        for i in range(2, 11):
            m[i] = m[i-1]*10+10**(i-1)
        # print(m)

        def get(num, length):
            if num == 0:
                return 0
            return m[max(length-1, 0)]*num + (10**max(length-1, 0) if num > 1 else 0) + (1 if num==1 else 0)
        s= str(n)
        length = len(s)
        ret = 0
        old = 0
        for i, c in enumerate(s):
            ret += get(int(c), length-i) + old * (int(c)*10**(length-i-1))
            if c == '1':
                old += 1
        return ret


def main():
    s = Solution()
    print(s.countDigitOne(13))
    print(s.countDigitOne(123456789))


if __name__ == "__main__":
    main()
