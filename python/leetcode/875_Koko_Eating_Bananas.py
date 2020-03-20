# /usr/bin/python2.7
# -*- coding:utf-8 -*-
import math


class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        def get_hours(piles, k):
            ret = 0
            for pile in piles:
                ret += math.ceil(pile*1.0 / k)
            return ret
        # print(get_hours(piles, 13))
        # print(get_hours(piles, 14))
        start = 1
        end = max(piles)
        mid = (start+end)/2
        hours_of_mid = get_hours(piles, mid)
        m = {}
        while start < end:
            if hours_of_mid == H:
                return mid
            elif hours_of_mid < H:
                if m.get(mid-1, None) is None:
                    buff = get_hours(piles, mid-1)
                    if  buff > H:
                        return mid
                    m[mid-1] = buff
                else:
                    if m[mid-1] > H:
                        return mid
                end = mid - 1
            else:
                start = mid + 1
            mid = (start+end)/2
            hours_of_mid = get_hours(piles, mid)
        return mid


def main():
    s = Solution()
    print(s.minEatingSpeed([3,6,7,11], H = 8))
    print(s.minEatingSpeed( [30,11,23,4,20], H = 6))
    print(s.minEatingSpeed([30,11,23,4,20], H = 5))
    print(s.minEatingSpeed([332484035, 524908576, 855865114, 632922376, 222257295, 690155293, 112677673, 679580077, 337406589, 290818316, 877337160, 901728858, 679284947, 688210097, 692137887, 718203285, 629455728, 941802184], 823855818))


if __name__ == "__main__":
    main()
