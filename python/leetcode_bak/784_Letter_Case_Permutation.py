# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        ret = [""]
        for c in S.lower():
            print(ret)
            if 'a' <= c <= 'z':
                for i in range(len(ret)):
                    ret[i] += c
                    ret.append(ret[i][:-1] + c.upper())
            else:
                for i in range(len(ret)):
                    ret[i] += c
        return ret


def main():
    s = Solution()
    print(s.letterCasePermutation("a1b2"))


if __name__ == "__main__":
    main()
