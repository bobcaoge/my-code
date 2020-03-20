# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if N == 1:
            return 0
        if K % 2 == 0:
            return 1-self.kthGrammar(N-1, int(K/2))
        return self.kthGrammar(N-1, int((K+1)/2))


def main():
    s = Solution()


if __name__ == "__main__":
    main()
