# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        dp_ones, dp_zeros = (1, 0) if S[0] == '0' else (0, 1)
        for i in range(1, len(S)):
            if S[i] == "1":
                buff_ones = min(dp_ones, dp_zeros)
                buff_zeros = dp_zeros+1
            else:
                buff_ones = min(dp_ones, dp_zeros)+1
                buff_zeros = dp_zeros
            dp_ones, dp_zeros = buff_ones, buff_zeros
        return min(dp_zeros, dp_ones)


def main():
    s = Solution()
    print(s.minFlipsMonoIncr("00100"))
    print(s.minFlipsMonoIncr("00110"))
    print(s.minFlipsMonoIncr("010110"))
    print(s.minFlipsMonoIncr("00011000"))

if __name__ == "__main__":
    main()
