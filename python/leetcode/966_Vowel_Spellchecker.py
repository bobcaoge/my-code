# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import re


class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        s = set(wordlist)
        m_of_case = {}
        m_of_vowels = {}
        for word in wordlist:
            buff = m_of_case.get(word.lower(), None)
            if not buff:
                m_of_case[word.lower()] = [word]
            else:
                buff.append(word)
            word_without_vowel = re.sub(r"[aeiouAEIOU]", " ",word).lower()
            buff = m_of_vowels.get(word_without_vowel, None)
            if not buff:
                m_of_vowels[word_without_vowel] = [word]
            else:
                buff.append(word)
        ret = [""]*len(queries)
        for i, word in enumerate(queries):
            if word in s:
                ret[i] = word
                continue
            buff = m_of_case.get(word.lower(), None)
            if buff:
                ret[i] = buff[0]
                continue
            buff = m_of_vowels.get(re.sub(r"[aeiouAEIOU]", " ",word).lower(), None)
            if buff:
                ret[i] = buff[0]
        return ret


def main():
    s = Solution()
    print(s.spellchecker(wordlist = ["KiTe","kite","hare","Hare"],
                         queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]))


if __name__ == "__main__":
    main()
