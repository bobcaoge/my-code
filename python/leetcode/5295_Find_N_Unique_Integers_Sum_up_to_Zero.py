# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        self.ret = []
        for i in range(n//2):
            self.ret.extend([i+1, -1-i])
        if n%2 != 0:
            self.ret.append(0)
        return self.ret




def main():
    s = Solution()


if __name__ == "__main__":
    main()
