# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def toHexspeak(self, num):
        """
        :type num: str
        :rtype: str
        """
        coll = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F', 0:'O', 1:'I'}
        num = int(num)
        ret = ""
        while num != 0:
            cur = num % 16
            if cur not in coll:
                return "ERROR"
            ret += coll[cur]
            num //= 16
        return ret[::-1]


def main():
    s = Solution()
    print(s.toHexspeak("257"))
    print(s.toHexspeak("3"))


if __name__ == "__main__":
    main()
