# /usr/bin/python3.6
# -*- coding:utf-8 -*-
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None:
            return 0

        substr = str(s[0])
        ret = 1
        for i in s:
            index = substr.rfind(i)
            if index == -1:
                substr += i
            else:
                substr = substr[index+1:] + i
            if len(substr) > ret:
                ret = len(substr)
        return ret



def main():
    s = Solution()
    num = s.lengthOfLongestSubstring("abcabcbb")
    print(num)


if __name__ == "__main__":
    main()
