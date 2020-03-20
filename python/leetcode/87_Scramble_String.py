# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):
            return False
        if len(s1) == len(s2) == 1:
            return s1 == s2
        m1 = [0]*128
        m2 = [0]*128
        for i, c in enumerate(s1):
            m1[ord(c)] += 1
            m2[ord(s2[i])] += 1
            if m1 == m2 and i != len(s1)-1 and self.isScramble(s1[:i+1],s2[:i+1]) and self.isScramble(s1[i+1:], s2[i+1:]):
                return True
        m1 = [0]*128
        m2 = [0]*128
        for i in range(len(s1)-1, -1, -1):
            m1[ord(s1[i])] += 1
            m2[ord(s2[len(s2)-1-i])] += 1
            if m1 == m2 and i != 0 and self.isScramble(s1[i:], s2[:len(s1)-i]) and self.isScramble(s1[:i], s2[len(s1)-i:]):
                return True
        return False



def main():
    s = Solution()
    print(s.isScramble("great", "great"))
    print(s.isScramble(s1 = "abcde", s2 = "caebd"))
    print(s.isScramble(s1 = "great", s2 = "rgeat"))
    print(s.isScramble("abcde", "cbaed"))
    print(s.isScramble('ab', 'ba'))
    print(s.isScramble("oatzzffqpnwcxhejzjsnpmkmzngneo",
                       "acegneonzmkmpnsjzjhxwnpqffzzto"))


if __name__ == "__main__":
    main()
