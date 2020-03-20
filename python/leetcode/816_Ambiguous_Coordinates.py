# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def get_legal_nums(self, s):
        if len(s) == 1:
            return [int(s)]
        ret = []
        if s.find("0") != 0:
            ret.append(s)
        for i in range(1, len(s)):
            if s[-1] != "0" and (s[0] != "0" or s[0] == "0" and i == 1):
                if int(s[:i]) == int(s[i:]) == 0:
                    continue
                ret.append(s[:i]+"."+s[i:])
        return ret

    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        S = S[1:len(S)-1]
        ret = []
        for i in range(1, len(S)):
            first = self.get_legal_nums(S[:i])
            second = self.get_legal_nums(S[i:])
            if first and second:
                for f in first:
                    ret.extend(["({0}, {1})".format(f, x) for x in second])
        return ret


def main():
    s = Solution()
    # print(s.ambiguousCoordinates("(1111)"))
    # print(s.ambiguousCoordinates("(123)"))
    # print(s.ambiguousCoordinates("(00123)"))
    print(s.ambiguousCoordinates("(00100)"))


if __name__ == "__main__":
    main()
