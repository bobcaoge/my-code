# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def queryString(self, S, N):
        """
        :type S: str
        :type N: int
        :rtype: bool
        """
        S = S[::-1]
        flag = [False]*(N+1)
        flag[0] = True
        for i in range(len(S)):
            total = 0
            for j in range(i, len(S)):
                if S[j] == "1":
                    total += 1 << j-i
                if total <= N:
                    flag[total] = True
        return all(flag)



def main():
    s = Solution()
    print(s.queryString("0110", 3))
    print(s.queryString("1111000101", 5))
    print(s.queryString("1", 1))


if __name__ == "__main__":
    main()
