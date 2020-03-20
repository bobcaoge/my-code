# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        flag = 10**(N-1)
        s = [ x for x in range(1, 10)]
        ret = []
        while s:
            num = s.pop()
            if num >= flag:
                ret.append(num)
            else:
                temp = num % 10
                if 0 <= temp + K < 10:
                    s.append(num*10 + temp+K)
                if K != 0 and 0 <= temp - K < 10:
                    s.append(num*10 + temp-K)
        return ret if N > 1 else ret + [0]



def main():
    s = Solution()
    print(s.numsSameConsecDiff(5, 2))


if __name__ == "__main__":
    main()
