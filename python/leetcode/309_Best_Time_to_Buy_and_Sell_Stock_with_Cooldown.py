# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        hold = -2**32
        not_hold_cooldown = -2**32
        not_hold = 0
        for price in prices:
            hold = max(hold, not_hold-price)
            not_hold = max(not_hold_cooldown, not_hold)
            not_hold_cooldown = hold+price
        return max(not_hold, not_hold_cooldown)




def main():
    s = Solution()
    print(s.maxProfit([1,2,3,0,2]))
    print(s.maxProfit([1,2,3,4,5,6,7,8,9]))


if __name__ == "__main__":
    main()
