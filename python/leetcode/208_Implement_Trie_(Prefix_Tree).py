# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Node(object):
    def __init__(self, value="", is_str=False):
        self.is_str = is_str
        self.value = value
        self.children = []


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word):
        """
        Inserts a word into the trie.
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

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        root = self.root
        length = 0
        for c in word:
            if not root.children:
                return False
            for child in root.children:
                if child.value == c:
                    root = child
                    length += 1
                    break
            else:
                return False
        if length == len(word) and root.is_str:
            return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        root = self.root
        length = 0
        for c in prefix:
            for child in root.children:
                if child.value == c:
                    root = child
                    length += 1
                    break
            else:
                return False
        if length == len(prefix):
            return True
        return False


def traverse(root, value):
    if root:
        if root.is_str:
            print(value+root.value)
        else:
            for child in root.children:
                traverse(child, value+root.value)


def main():
    prefix_tree = Trie()
    prefix_tree.insert("hello")
    print(prefix_tree.search("hello"))
    print(prefix_tree.search("he"))
    print(prefix_tree.startsWith("he"))
    print(prefix_tree.startsWith("hellol"))
    traverse(prefix_tree.root, "")


if __name__ == "__main__":
    main()
