# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        for i in range(1, n):
            if str(i).count('0') == 0 and str(n-i).count('0') == 0:
                return [i, n-i]



def main():
    s = Solution()


if __name__ == "__main__":
    main()
