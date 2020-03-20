# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.characters = characters
        self.ret = []
        self.dfs("", 0, combinationLength)
        self.pos = 0

    def dfs(self, s, pos, length):
        if len(s) == length:
            self.ret.append(s)
            return
        if pos > len(self.characters):
            return
        for i in range(pos, len(self.characters)):
            self.dfs(s+self.characters[i], i+1, length)
    def next(self):
        """
        :rtype: str
        """
        ret = self.ret[self.pos]
        self.pos += 1
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.pos < len(self.ret)



# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()


def main():
    s = CombinationIterator("abcdefg", 3)
    while s.hasNext():
        print(s.next())
    s = CombinationIterator("abbc", 3)
    while s.hasNext():
        print(s.next())


if __name__ == "__main__":
    main()
