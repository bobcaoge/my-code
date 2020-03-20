# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):


    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        before = set()
        before.add(beginWord)
        length = 1
        w = "abcdefghijklmnopqrstuvwxyz"
        wordList = set(wordList)
        while not before.__contains__(endWord):
            after = set()
            for word_before in before:
                for i in range(len(word_before)):
                    for c in w:
                        word = word_before[:i]+c+word_before[i+1:]
                        if word in wordList:
                            after.add(word)
                            wordList.remove(word)
            if not after:
                return 0
            before = after
            length += 1
        return length




def main():
    s = Solution()


if __name__ == "__main__":
    main()
