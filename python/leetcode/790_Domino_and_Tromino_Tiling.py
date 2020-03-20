# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        md = 10**9+7
        v = [0,1,2,5]

        if N < 4:
            return v[N]

        for i in range(4, N+1):
            a = 2*v[-1]+v[-3]
            v[0], v[1], v[2], v[3] = v[1], v[2],v[3], a
        return v[-1]




def main():
    s = Solution()
    print(s.numTilings(6))
    print(s.numTilings(6))


if __name__ == "__main__":
    main()
