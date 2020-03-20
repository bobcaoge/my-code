# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        indexes_of_c = [-2**32]
        for index, s in enumerate(S):
            if s == C:
                indexes_of_c.append(index)
        indexes_of_c.append(2**32)
        before = 0
        back = 1
        ret = []
        for index, s in enumerate(S):
            ret.append(min(index-indexes_of_c[before], indexes_of_c[back]-index))
            if s == C:
                before += 1
                back += 1
        return ret




def main():
    s = Solution()


if __name__ == "__main__":
    main()
