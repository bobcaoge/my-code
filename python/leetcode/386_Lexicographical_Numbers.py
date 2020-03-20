# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def compare(num1, num2):
            n1 = str(num1)
            n2 = str(num2)
            if n1 == n2:
                return 0
            if n1 > n2:
                return 1
            return -1
        return sorted([x+1 for x in range(n)], compare)


def main():
    s = Solution()


if __name__ == "__main__":
    main()
