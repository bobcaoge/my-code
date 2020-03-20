# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = list(s)
        vowels = "aeiouAEIOU"
        start = 0
        end = len(s) - 1
        while start < end:
            if vowels.__contains__(s_list[start]) and vowels.__contains__(s_list[end]):
                s_list[start] , s_list[end] = s_list[end], s_list[start]
                start += 1
                end -= 1
            else:
                if not vowels.__contains__(s_list[start]):
                    start += 1
                if not vowels.__contains__(s_list[end]):
                    end -= 1
        return "".join(s_list)


def main():
    s = Solution()


if __name__ == "__main__":
    main()
