# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    k = 0
    s = []

    def buffer(self, base):
        cur = self.k / base
        cur = int(cur)
        self.k -= base*cur
        ret = self.s[cur]
        self.s = self.s[:cur]+self.s[cur+1:]
        return ret

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        jiecheng_of_n_1 = 1
        for i in range(1, n):
            jiecheng_of_n_1 *= i
        ret = []
        self.s = [j for j in range(1, n+1)]
        self.k = k-1
        for i in range(n-1):
            ret.append(str(self.buffer(jiecheng_of_n_1)))
            jiecheng_of_n_1 = jiecheng_of_n_1 / (n-i-1)

        return "".join(ret)+str(self.s[0])


def main():
    s = Solution()
    print(s.getPermutation(3, 3))
    print(s.getPermutation(4, 9))
    print(s.getPermutation(1, 1))
    print(s.getPermutation(2, 2))


if __name__ == "__main__":
    main()
