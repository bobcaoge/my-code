# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def get(self, s):
        nums_s = s.split("+")
        return int(nums_s[0]), int(nums_s[1][:-1])

    def complexNumberMultiply(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: str
        """
        a, b = self.get(s1)
        c, d = self.get(s2)
        return str(a*c-b*d)+"+"+str(b*c+a*d)+"i"




def main():
    s = Solution()


if __name__ == "__main__":
    main()
