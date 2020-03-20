# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """

        def f(a, b, m):
            length_a = len(a)
            length_b = len(b)
            index = 0
            while index < length_a and index < length_b:
                if m[a[index]] < m[b[index]]:
                    return True
                elif m[a[index]] == m[b[index]]:
                    index += 1
                else:
                    return False
            if length_a <= length_b:
                return True
            else:
                return False

        m = {}
        for index, c in enumerate(order):
            m[c] = index

        for i in range(len(words) - 1):
            if not f(words[i], words[i + 1], m):
                return False
        return True



def main():
    s = Solution()


if __name__ == "__main__":
    main()
