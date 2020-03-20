# /usr/bin/python3.6
# -*- coding:utf-8 -*-

import copy
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        m = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        if not digits:
            return []
        ret = [c for c in m[digits[0]]]
        for c in digits[1:]:
            length = len(ret[0])
            leng = len(ret)
            for index, x in enumerate(m[c]):
                # print(ret)
                if index == 0:
                    ret = [s+x for s in ret]
                else:
                    ret += [s[0:length]+x for s in ret[:leng]]
        return ret
    def letterCombinations1(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        m = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        if not digits:
            return []
        ret = [""]
        for c in digits:
            buff = copy.deepcopy(ret)
            ret = []
            for x in m[c]:
                ret += [s+x for s in buff]
        return ret

def main():
    s = Solution()
    print(s.letterCombinations("23"))


if __name__ == "__main__":
    main()
