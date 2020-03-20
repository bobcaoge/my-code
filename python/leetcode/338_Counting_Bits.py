# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        return [bin(i).count("1") for i in range(num+1)]



def main():
    s = Solution()


if __name__ == "__main__":
    main()
