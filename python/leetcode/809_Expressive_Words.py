# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import copy


class Solution(object):
    def get_data(self, s):
        keep = []
        old = s[0]
        num = 1
        for i in range(1, len(s)):
            if s[i] == old:
                num += 1
            else:
                keep.append([old, num])
                num = 1
                old = s[i]
        keep.append([old, num])
        return keep

    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        ret = 0
        keep = self.get_data(S)
        for word in words:
            if not word:
                continue
            bak = copy.deepcopy(keep)
            cur = self.get_data(keep)
            if len(bak) != len(cur):
                continue
            for i in range(len(bak)):
                if bak[i][0] == cur[i][0] and bak[i][1] == cur[i][1] or bak[i][1] > cur[i][1] and bak[i][1] >= 3:
                    continue
                else:
                    break
            else:
                ret += 1
        return ret


def main():
    s = Solution()
    print(s.expressiveWords("dddiiiinnssssssoooo",
                            ["dinnssoo","ddinso","ddiinnso","ddiinnssoo","ddiinso","dinsoo","ddiinsso","dinssoo","dinso"]))


if __name__ == "__main__":
    main()
