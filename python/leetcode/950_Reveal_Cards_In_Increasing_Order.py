# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import queue


class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort()
        if len(deck) <= 2:
            return deck
        q = queue.Queue()
        for i in range(len(deck)-1, -1, -1):
            if q.empty():
                q.put(deck[i])
            else:
                to_put = q.get()
                q.put(to_put)
                q.put(deck[i])
        ret = []
        while not q.empty():
            ret.append(q.get())
        ret.reverse()
        return ret


def main():
    s = Solution()
    print(s.deckRevealedIncreasing([17,13,11,2,3,5,7]))


if __name__ == "__main__":
    main()
