# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    m = {}
    used = []

    def recursion(self, desired_total):
        """
        :type self.used: list[bool]
        :type self.m: dict
        :type desired_total: int
        :return:
        """
        if desired_total <= 0:
            return False
        key = str(self.used)
        if not self.m.keys().__contains__(key):
            for i in range(1, len(self.used)):
                if not self.used[i]:
                    self.used[i] = True
                    if not self.recursion(desired_total-i):
                        self.m[key] = True
                        self.used[i] = False
                        return True
                # self.m[key] = False
                    self.used[i] = False
            self.m[key] = False
        return self.m[key]

    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if (maxChoosableInteger+1)*maxChoosableInteger /2 < desiredTotal:
            return False
        if desiredTotal <= 0:
            return True
        self.m = {}
        self.used = [False]*(maxChoosableInteger+1)
        return self.recursion(desiredTotal)


def main():
    s = Solution()
    print(s.canIWin(10, 11))


if __name__ == "__main__":
    main()
