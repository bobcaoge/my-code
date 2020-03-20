# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def isIsomorphic1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map_table = {}
        for i in range(len(s)):
            a = s[i]
            b = t[i]
            if not map_table.keys().__contains__(a):
                if map_table.values().__contains__(b):
                    return False
                map_table[a] = b
            else:
                if map_table[a] != b:
                    return False

        print(map_table)
        return True
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m1 = [0]*256
        m2 = [0]*256
        for i in range(len(s)):
            if m1[ord(s[i])] != m2[ord(t[i])]:
                return False
            m1[ord(s[i])] = i+1
            m2[ord(t[i])] = i+1
        return True


def main():
    s = Solution()
    print(s.isIsomorphic("ab", "aa"))


if __name__ == "__main__":
    main()
