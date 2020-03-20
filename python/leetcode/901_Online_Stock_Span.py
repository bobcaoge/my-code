# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class StockSpanner(object):

    def __init__(self):
        self.prices = [-1]
        self.dp = [0]

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        self.dp.append(self.dp[-1]+1 if price >= self.prices[-1] else 1)
        self.prices.append(price)
        i = len(self.prices) - 1
        ret = 0
        while price >= self.prices[i] and i > 0:
            ret += self.dp[i]
            i -= self.dp[i]
        return ret




def main():
    s = StockSpanner()
    for i in [100, 80, 60, 70, 60, 75, 85]:
        print(s.next(i))


if __name__ == "__main__":
    main()
