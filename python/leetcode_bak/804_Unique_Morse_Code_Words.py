# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import re


class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        tran = set()
        for word in words:
            s = ""
            for c in word:
                s += morse_codes[ord(c)-97]
            tran.add(s)
        return len(tran)

def main():
    s = Solution()
    print(s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))


if __name__ == "__main__":
    main()
