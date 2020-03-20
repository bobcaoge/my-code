# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels_set = set(J)
        ret = 0
        for c in S:
            if c in jewels_set:
                ret += 1
        return ret
    def numJewelsInStones1(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels_map = {}
        for c in J:
            jewels_map[c] = 1
        ret = 0
        for c in S:
            if jewels_map.get(c, 0) == 1:
                ret += 1
        return ret


def main():
    s = Solution()


if __name__ == "__main__":
    main()
