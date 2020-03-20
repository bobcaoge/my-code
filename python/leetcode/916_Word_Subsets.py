# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import collections


class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        ret = []
        info_of_B = {}
        for word_of_B in B:
            cur = collections.Counter(word_of_B)
            for c in word_of_B:
                if info_of_B.get(c, 0) < cur[c]:
                    info_of_B[c] = cur[c]

        for word_of_A in A:
            a = collections.Counter(word_of_A)
            for letter, num in info_of_B.items():
                if a.get(letter, 0) < num:
                    break
            else:
                ret.append(word_of_A)
        return ret



def main():
    s = Solution()


if __name__ == "__main__":
    main()
