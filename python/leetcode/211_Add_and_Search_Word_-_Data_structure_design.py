# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Node(object):
    def __init__(self, value="", is_str=False):
        self.is_str = is_str
        self.value = value
        self.children = []


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        root = self.root
        for c in word:
            for child in root.children:
                if child.value == c:
                    root = child
                    break
            else:
                node = Node(value=c)
                root.children.append(node)
                root = node
        root.is_str = True

    def search(self, word, root=None):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :type root: Node
        :rtype: bool
        """
        if not root:
            root = self.root
        if not word:
            if root.is_str:
                return True
            return False
        if root:
                flag = False
                for child in root.children:
                    if word[0] == "." or word[0] == child.value:
                        flag = flag or self.search(word[1:], child)
                return flag
        return False


def main():
    pass


if __name__ == "__main__":
    main()
