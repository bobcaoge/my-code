# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        ret = []
        last = -1
        S += " "
        for i in range(len(S)-1):
            if S[i] != S[i+1]:
                if i - last >= 3:
                    ret.append([last+1, i])
                last = i
        return ret


def main():
    s = Solution()


if __name__ == "__main__":
    main()
