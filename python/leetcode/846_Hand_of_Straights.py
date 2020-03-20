# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import collections


class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        if len(hand) % W != 0:
            return False
        m = collections.Counter(hand)
        s = sorted(set(hand))
        for num in s:
            to_minus = m[num]
            if to_minus > 0:
                for j in range(W):
                    if m.get(num+j, 0) < to_minus:
                        return False
                    m[num+j] -= to_minus
            elif to_minus < 0:
                return False
        return True


def main():
    s = Solution()
    print(s.isNStraightHand([1,2,3,6,2,3,4,7,8], W = 3))
    print(s.isNStraightHand([1,3,4,5], 4))


if __name__ == "__main__":
    main()
