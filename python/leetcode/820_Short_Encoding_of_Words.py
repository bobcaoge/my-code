# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Node(object):
    def __init__(self, val):
        self.val = val
        self.children = []

def insert(root, s):
    flag = False
    for c in s:
        for child in root.children:
            if c == child.val:
                root = child
                break
        else:
            flag = True
            child = Node(c)
            root.children.append(child)
            root = child
    return flag



class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def compare(s1, s2):
            if len(s1) > len(s2):
                return -1
            return 1
        words.sort(compare)
        root = Node("")
        ret = 0
        for word in words:
            if insert(root, word[::-1]):
                ret += len(word)+1
        return ret


def main():
    s = Solution()
    print(s.minimumLengthEncoding(["time", "me", "bell"]))


if __name__ == "__main__":
    main()
