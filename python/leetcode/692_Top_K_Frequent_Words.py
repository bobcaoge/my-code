# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import heapq
import collections


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        m = {}
        for word in words:
            m[word] = m.get(word, 0) + 1
        heap = [[-num, word] for word, num in m.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]


    def topKFrequent2(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        m = {}
        for word in words:
            m[word] = m.get(word, 0) + 1
        return [word for _ ,word in sorted([[-num, word] for word, num in m.items()])[:k]]
    def topKFrequent3(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        return [word for _ ,word in sorted([[-num, word] for word, num in collections.Counter(words).items()])[:k]]


def main():
    s = Solution()
    print(s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"],
    2))
    print(s.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
    4))


if __name__ == "__main__":
    main()
