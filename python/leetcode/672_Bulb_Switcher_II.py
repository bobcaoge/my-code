# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        s = set()
        s.add(tuple((0 for _ in range(n))))
        n = min(n, 10)
        for i in range(m):
            buff = set()
            for bulbs in s:
                # flip all
                buff.add(tuple([1-x for x in bulbs]))
                # flip even
                buff.add(tuple([x if index % 2 == 0 else 1-x for index, x in enumerate(bulbs)]))
                # flip odd
                buff.add(tuple([x if index % 2 != 0 else 1-x for index, x in enumerate(bulbs)]))
                # flip 3K+1
                buff.add(tuple([1-x if (index%3 == 0) else x for index, x in enumerate(bulbs)]))
            s = buff
        return len(s)


def main():
    s = Solution()
    print(s.flipLights(10, 4))
    print(s.flipLights(1000, 1000))


if __name__ == "__main__":
    main()
