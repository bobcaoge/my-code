# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        if amount < min(coins):
            return -1
        amounts = [amount+1]*(amount+1)
        amounts[0] = 0
        for i in range(1, amount+1):
            if i in coins:
                amounts[i] = 1
            else:
                for coin in coins:
                    if i - coin > 0:
                        amounts[i] = min(amounts[i], amounts[i-coin]+1)
        # print(amounts)
        return amounts[-1] if amounts[-1] <= amount else -1


def main():
    s = Solution()
    print(s.coinChange([1,2,5], 12))
    print(s.coinChange([1,4,5], 12))
    print(s.coinChange([1, 2**32-1], 2))
    print(s.coinChange([2], 3))
    print(s.coinChange([2], 2**32))


if __name__ == "__main__":
    main()
