# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if not trust:
            return N
        trust_people = set()
        m = {}
        for x, y in trust:
            m[y] = m.get(y, 0) + 1
            trust_people.add(x)
        if N == len(trust_people):
            return -1
        for key, value in m.items():
            if value == N-1:
                return key
        return -1

def main():
    s = Solution()


if __name__ == "__main__":
    main()
