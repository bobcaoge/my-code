# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        table = {}
        for c in list("qwertyuiopQWERTYUIOP"):
            table[c] = 1
        for c in list("asdfghjklASDFGHJKL"):
            table[c] = 2
        for c in list("zxcvbnmZXCVBNM"):
            table[c] = 3
        ret = []
        for word in words:
            buffer = 0
            for c in word:
                buffer += table[c]
            if buffer/len(word) == table[word[0]]:
                ret.append(word)
        return ret


def main():
    s = Solution()
    print(s.findWords(["Hello", "Alaska", "Dad", "Peace"]))
    print(s.findWords(["qz","wq","asdddafadsfa","adfadfadfdassfawde"]))

if __name__ == "__main__":
    main()
