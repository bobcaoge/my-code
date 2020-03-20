# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        left = [0]*len(prices)
        right = [0]*len(prices)
        small = prices[0]
        big = prices[-1]
        last_small = 0
        last_big = 0
        for i in range(len(prices)):
            small = min(small, prices[i])
            big = max(big, prices[-i-1])
            left[i] = max(prices[i] - small, last_small)
            right[-i-1] = max(big - prices[-i-1], last_big)
            last_small, last_big = left[i], right[-1-i]

        ret = 0
        for i in range(len(left)):
            ret = max(left[i]+(right[i+1] if i+1 < len(right) else 0), ret)
        return ret


def main():
    s = Solution()
    print(s.maxProfit([3,3,5,0,0,3,1,4]))
    print(s.maxProfit([1,2,3,4,5]))
    print(s.maxProfit([7,6,4,3,1]))
    print(s.maxProfit([3,2,6,5,0,3]))



if __name__ == "__main__":
    main()
