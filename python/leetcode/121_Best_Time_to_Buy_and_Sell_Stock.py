# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        stack = [prices[0]]
        max = 0
        for i in range(1, len(prices)):
            # print(stack, i, prices[i], max)
            while stack and prices[i] < stack[-1]:
                stack.pop()
            stack.append(prices[i])
            if stack[-1] - stack[0] > max:
                max = stack[-1] - stack[0]
            # print(stack, i, prices[i], max)
        return max


def main():
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
    print(s.maxProfit([7,6,4,3,1]))
    print(s.maxProfit([]))
    print(s.maxProfit([1]))
    print(s.maxProfit([3,2,6,5,0,3]))
    print(s.maxProfit([2,1,2,1,0,1,2]))

if __name__ == "__main__":
    main()
