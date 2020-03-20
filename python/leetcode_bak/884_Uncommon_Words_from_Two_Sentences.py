# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        a = A.split(" ")
        b = B.split(" ")
        map_a = {}
        for word in a:
            map_a[word] = map_a.get(word, 0) + 1
        map_b = {}
        for word in b:
            map_b[word] = map_b.get(word, 0) + 1
        ret = []
        for word, time in map_a.items():
            if time == 1 and map_b.get(word, 0) == 0:
                ret.append(word)
        for word, time in map_b.items():
            if time == 1 and map_a.get(word, 0) == 0:
                ret.append(word)
        return ret



def main():
    s = Solution()


if __name__ == "__main__":
    main()
