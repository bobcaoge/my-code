# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length <= 1:
            return 0
        sum = 0
        cur_stock = prices[0]
        i = 1
        while i < length:
            # print(i)
            if prices[i] > cur_stock:
                # print("==", prices[i], cur_stock, i)
                if i+1 < length:
                    if prices[i+1] < prices[i]:
                        sum += prices[i] - cur_stock
                        cur_stock = prices[i+1]
                        i += 2
                    else:
                        i += 1
                else:
                    sum += prices[i] - cur_stock

                    break

            else:
                cur_stock = prices[i]
                i += 1

        return sum


def main():
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
    print(s.maxProfit([7, 6, 4, 3, 1]))
    print(s.maxProfit([]))
    print(s.maxProfit([1]))
    print(s.maxProfit([3, 2, 6, 5, 0, 3]))
    print(s.maxProfit([2, 1, 2, 1, 0, 1, 2]))


if __name__ == "__main__":
    main()
