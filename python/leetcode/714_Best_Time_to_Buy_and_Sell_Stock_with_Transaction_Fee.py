# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def maxProfit1(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        dp = [0 for _ in range(len(prices))]
        for i in range(len(prices)):
            for j in range(i):
                dp[i] = max(dp[i], dp[j]+prices[i]-prices[j]-fee, dp[j])
        return dp[-1]

    def maxProfit(self, prices, fee):
        old_stock_in_hand = -prices[0]
        old_stock_not_in_hand = 0
        for price in prices[1:]:
            cur_stock_in_hand = max(old_stock_in_hand, old_stock_not_in_hand-price)
            cur_stock_not_in_hand = max(old_stock_not_in_hand, old_stock_in_hand+price-fee)
            old_stock_in_hand, old_stock_not_in_hand = cur_stock_in_hand, cur_stock_not_in_hand
        return old_stock_not_in_hand


def main():
    s = Solution()
    print(s.maxProfit(prices = [1, 3, 2, 8, 4, 9], fee = 2))
    print(s.maxProfit([1,3,2,8,4,9,4,6,2,8,1,6,4,2,4,5,5,9], 2))
    with open("./data.txt", "r") as f:
        prices = eval(f.readline())
        fee = eval(f.readline())
        print(s.maxProfit(prices,fee))



if __name__ == "__main__":
    main()
