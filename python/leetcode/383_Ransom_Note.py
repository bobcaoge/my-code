# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def canConstruct1(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) > len(magazine):
            return False
        m1 = [0]*26
        m2 = [0]*26
        for c in ransomNote:
            m1[ord(c)-97] += 1
        for c in magazine:
            m2[ord(c)-97] += 1
        print(m1)
        print(m2)
        for i in range(26):
            if m1[i] != 0 and m1[i] > m2[i]:
                return False
        return True

    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) > len(magazine):
            return False
        m1 = [0]*26

        for c in magazine:
            m1[ord(c)-97] += 1
        for c in ransomNote:
            index = ord(c) - 97
            m1[index] -= 1
            if m1[index] < 0:
                return False
        return True




def main():
    s = Solution()
    s.canConstruct("aa", "aab")


if __name__ == "__main__":
    main()
