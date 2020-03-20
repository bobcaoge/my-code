# /usr/bin/python3.6
# -*- coding:utf-8 -*-


import re
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        pattern = re.compile(r"\w+")
        banned = set(banned)
        m = {}
        most_frequency = 0
        most_common_word = ""
        for word in pattern.findall(paragraph.lower()):
            if word not in banned:
                m[word] = m.get(word, 0) + 1
                if m[word] > most_frequency:
                    most_common_word, most_frequency = word, m[word]
        # print(m)
        return most_common_word


def main():
    s = Solution()


if __name__ == "__main__":
    main()
