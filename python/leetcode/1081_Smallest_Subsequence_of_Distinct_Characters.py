# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import heapq


class Solution(object):
    visited = {}
    def recursion(self, text, last):
        if text == "":
            return last
        if self.visited.get((text, last), None):
            return self.visited[(text, last)]
        length = len(set(text))
        cur = "zz"
        for index, c in enumerate(text):
            buff = self.recursion(text[index+1:].replace(text[index], ""), last+text[index])
            if buff < cur:
                cur = buff
        self.visited[(text, last)] = cur
        return cur

    def smallestSubsequence(self, text):
        """
        :type text: str
        :rtype: str
        """
        last = {c:i for i, c in enumerate(text)}
        stack = []
        for i, c in enumerate(text):
            if c in stack:
                continue
            while stack and stack[-1] > c and i < last[stack[-1]]:
                stack.pop()
            stack.append(c)
        return "".join(stack)




def main():
    s = Solution()
    # print(s.smallestSubsequence("abcd"))
    print(s.smallestSubsequence("cdadabcc"))
    print(s.smallestSubsequence("leetcode"))
    print(s.smallestSubsequence("bdfecedcbfcfeaaffdbaeeabadbbbddddcafdfeeeebfcdabcfaadecddccdefcabedbebbdcbdfefeffcbbeaefaeefeeceadea"))
    print(s.smallestSubsequence("ddeeeccdce"))
    print(s.smallestSubsequence("pblspykdpqfhcfcirkrhbbfbnqagshfqrrkcjpsuaytjfwyhjpubttxkkpswuvoiicsnkxiyhsyqrqecsiabhvjfodpkdgcgdceobyfonnurqxvstxkgsagnosvfjgsnylyhbjcrkgaylgxxxmghfbpfqwpplntrrogtkapbpkkwkdxgrfmikdlcftuyywrsnfasxgiw"))


if __name__ == "__main__":
    main()
