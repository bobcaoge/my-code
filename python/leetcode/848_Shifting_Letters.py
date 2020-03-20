# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        old = 0
        length = len(shifts)
        for i in range(length-1, -1, -1):
            old += shifts[i]
            shifts[i] = old % 26
        ret = []
        for i, shift in enumerate(shifts):
            ret.append(str(chr((ord(S[i])-97+shift)%26+97)))
        return "".join(ret)


def main():
    s = Solution()
    print(s.shiftingLetters("abc", [3,5,9]))


if __name__ == "__main__":
    main()
