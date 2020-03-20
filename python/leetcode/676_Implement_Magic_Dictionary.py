# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dictionary = set()


    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: None
        """
        self.dictionary |= set(dict)


    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for i in range(len(word)):
            for j in range(97, 97+26):
                if j != ord(word[i]) and word[:i]+str(chr(j))+word[i+1:] in self.dictionary:
                    return True
        return False




# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)


def main():
    pass


if __name__ == "__main__":
    main()
