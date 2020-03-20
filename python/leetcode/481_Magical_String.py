# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n <= 3 :
            return 1
        ret = 1
        pos = 2
        s = [1,2,2]
        while len(s) < n:
            if s[pos] == 2:
                if s[-1] == 1:
                    s.extend([2, 2])
                else:
                    s.extend([1, 1])
                    ret += 2
            else:
                if s[-1] == 1:
                    s.append(2)
                else:
                    s.append(1)
                    ret += 1
            pos += 1
        if len(s) > n and s[-1] == 1:
            ret -= 1
        return ret


def main():
    s = Solution()
    print(s.magicalString(10000))
    print(s.magicalString(4))


if __name__ == "__main__":
    main()
