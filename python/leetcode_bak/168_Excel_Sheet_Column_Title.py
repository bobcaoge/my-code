# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 1:
            return

        # ret = str(chr(n%26 + 64))
        # n = int(n/26)
        ret = ""
        while n > 26:
            # print(n%26)
            buffer = n % 26
            if buffer == 0:
                ret += 'z'
                n = int(n/26) - 1
            else:
                ret = str(chr(n%26 + 64)) + ret
                n = int(n/26)
        # print(n)
        ret = str(chr(n + 64)) + ret

        return ret



def main():
    s = Solution()
    for i in range(26, 50):
        print(s.convertToTitle(i))
    print(s.convertToTitle(701))
    print(s.convertToTitle(28))
    print(s.convertToTitle(52))


if __name__ == "__main__":
    main()
