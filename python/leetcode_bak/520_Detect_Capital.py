# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word == word.upper() or word == word.lower():
            return True
        if 'A' <= word[0] <= 'Z' and len(word) > 1 and word[0]+word[1:].lower() == word:
            return True
        return False


def main():
    s = Solution()


if __name__ == "__main__":
    main()
