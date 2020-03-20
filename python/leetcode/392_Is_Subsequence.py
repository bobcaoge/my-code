# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        index_of_s = 0
        index_of_t = 0
        while index_of_t < len(t) and index_of_s < len(s):
            if t[index_of_t] == s[index_of_s]:
                index_of_s += 1
            index_of_t += 1
        return index_of_s == len(s)





def main():
    s = Solution()
    print(s.isSubsequence("abc", t = "ahbgdc"))


if __name__ == "__main__":
    main()
