# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import re

class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        m = {}
        for c in licensePlate.lower():
            if 'a'<= c <= 'z':
                m[c] = m.get(c, 0) + 1
        ret = ""
        for word in words:
            buffer = word.lower()
            flag = True
            for c, num in m.items():
                if buffer.count(c) < num:
                    flag = False
                    break
            if flag:
                ret = word if ret == "" or len(word) < len(ret) else ret
        return ret




def main():
    s = Solution()


if __name__ == "__main__":
    main()
