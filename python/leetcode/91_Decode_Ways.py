# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def buffer(self, s, i, flag):
        if i == len(s):
            return 0
        if len(s)-1 == i :
            if flag and int(s[i]) != 0:
                return 1
            if not flag and 9 < int(s[i-1])*10 + int(s[i]) < 27:
                return 1
        if flag:
            if int(s[i]) > 0 :
                return self.buffer(s, i+1, True) + self.buffer(s, i+1, False)
            return 0
        else:
            num = int(s[i-1])*10 + int(s[i])
            if 9 < num < 27:
                return self.buffer(s, i+1, True)
            return 0

    def numDecodings1(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        return self.buffer(s, 0, True)

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        if s[0] == "0":
            return 0

        old_not_used = 1
        old_used = 1

        for index in range(1, len(s)):
            cur = int(s[index])
            last = int(s[index-1])
            cur_used = 0
            if 9 < last*10 + cur < 27:
                cur_used += old_not_used

            cur_not_used = 0
            if cur > 0:
                cur_used += old_used
                cur_not_used = old_used
            old_used = cur_used
            old_not_used = cur_not_used

        return old_used


def main():
    s = Solution()
    print(s.numDecodings("12"))
    print(s.numDecodings("226"))
    print(s.numDecodings("22226"))
    print(s.numDecodings("222222222226"))
    print(s.numDecodings("222022022226"))
    print(s.numDecodings("220220222260"))
    print(s.numDecodings("9371597631128776948387197132267188677349946742344217846154932859125134924241649584251978418763151253"))
    print(s.numDecodings("0"))


if __name__ == "__main__":
    main()
