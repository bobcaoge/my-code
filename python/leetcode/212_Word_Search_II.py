# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TrieNode(object):
    def __init__(self, value):
        self.val = value
        self.children = []
        self.is_end = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode("")

    def add(self, word):
        cur = self.root
        for c in word:
            for child in cur.children:
                if c == child.val:
                    cur = child
                    break
            else:
                cur.children.append(TrieNode(c))
                cur = cur.children[-1]
        cur.is_end = True


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board:
            return []
        self.trie = Trie()
        for word in words:
            self.trie.add(word)
        row = len(board)
        col = len(board[0])
        self.ret = []
        def dfs(cur_trie, i, j, cur_word):
            if 0<= i < row and 0<= j < col:
                for child in cur_trie.children:
                    if board[i][j] == child.val:
                        if child.is_end:
                            self.ret.append(cur_word+board[i][j])
                        buff = board[i][j]
                        board[i][j] = '0'
                        for di, dj in ((-1, 0), (1, 0),(0, -1),(0, 1)):
                            dfs(child, i+di, j+dj, cur_word+buff)
                        board[i][j] = buff
                        break
        for i in range(row):
            for j in range(col):
                dfs(self.trie.root, i, j, "")
        return list(set(self.ret))


def main():
    s = Solution()
    print(s.findWords(board = [
        ['o','a','a','n'],
        ['e','t','a','e'],
        ['i','h','k','r'],
        ['i','f','l','v']
    ],
    words = ["oath","pea","eat","rain"]))


if __name__ == "__main__":
    main()
