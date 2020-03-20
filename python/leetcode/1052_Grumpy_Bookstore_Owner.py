# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        length = len(customers)
        dp_L = [0]*length
        dp_R = [0]*length
        old_L = 0
        old_R = 0
        for i in range(length):
            old_L += customers[i] if grumpy[i] != 1 else 0
            old_R += customers[length-1-i] if grumpy[length-1-i] != 1 else 0
            dp_L[i] = old_L
            dp_R[length-1-i] = old_R
        ret = 0
        cur = 0

        for i in range(length):
            cur += customers[i]
            if i+1 >= X:
                ret = max(ret, (dp_L[i-X] if i-X>= 0 else 0)+cur+(dp_R[i+1] if i+1 < length else 0))
                cur -= customers[i-X+1]
        return ret


def main():
    s = Solution()
    print(s.maxSatisfied( customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3))


if __name__ == "__main__":
    main()
