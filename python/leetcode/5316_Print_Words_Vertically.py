# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        s = s.split(' ')
        length = max([len(x) for x in s])
        ret = []
        for i in range(length):
            ret.append(''.join([(x[i] if i < len(x) else ' ') for x in s ]).rstrip(' '))
        return ret


def main():
    s = Solution()
    print(s.printVertically("TO BE OR NOT TO BE"))


if __name__ == "__main__":
    main()
