# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ret = {}
        for i in range(0, len(s) - 9):
            cur = s[i:i+10]
            ret[cur] = ret.get(cur, 0) + 1

        return [key for key, value in ret.items() if value > 1]


def main():
    s = Solution()
    print(s.findRepeatedDnaSequences("AAAAAAAAAAA"))


if __name__ == "__main__":
    main()
