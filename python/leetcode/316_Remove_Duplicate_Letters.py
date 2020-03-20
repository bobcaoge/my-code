# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def removeDuplicateLetters(self, s):
        for c in sorted(set(s)):
            suffix = s[s.index(c):]
            if set(suffix) == set(s):
                b = c + self.removeDuplicateLetters(suffix.replace(c, ''))
                return b
        return ''




def main():
    s = Solution()
    print(s.removeDuplicateLetters('cac'))
    print(s.removeDuplicateLetters('dcba'))
    # print(s.removeDuplicateLetters("lkjkjhojadfukjfasdsdaf"))
    # print(s.removeDuplicateLetters('bcabc'))
    print(s.removeDuplicateLetters('cbacdcbc'))


if __name__ == "__main__":
    main()
