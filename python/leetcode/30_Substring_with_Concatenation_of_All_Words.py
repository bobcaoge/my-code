# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import collections


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        length_of_word = len(words[0])
        m = collections.Counter(words)
        ret = []
        for j in range(length_of_word):
            i = j
            before = i
            cur = collections.Counter()
            while i < len(s):
                word = s[i:i+length_of_word]
                cur[word] += 1
                while cur[word] > m[word]:
                    cur[s[before:before+length_of_word]] -= 1
                    before += length_of_word
                if cur[word] == 0:
                    del cur[word]
                if cur == m:
                    ret.append(before)
                i += length_of_word
        return ret


def main():
    s = Solution()
    # print(s.findSubstring("bfbfbf", ['b', 'f']))
    # print(s.findSubstring("wordgoodgoodgoodbestword",["word","good","best","word"]))
    # print(s.findSubstring("wordgoodgoodgoodbestword",["word","good","best","good"]))
    print(s.findSubstring("barfoothefoobarman",["foo","bar"]))


if __name__ == "__main__":
    main()
