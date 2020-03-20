# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.queens = [0]*n
        def is_valid(j, num):
            for i in range(j):
                if abs(num-self.queens[i]) == abs(j-i) or num == self.queens[i]:
                    return False
            return True
        self.ret = []

        def manager(i):
            if i == n:
                res = [["." for __ in range(n)] for _ in range(n)]
                for k in range(n):
                    res[k][self.queens[k]] = 'Q'
                self.ret.append(["".join(x) for x in res])
                return
            for j in range(n):
                if is_valid(i, j):
                    self.queens[i] = j
                    manager(i+1)
        manager(0)
        return self.ret


def main():
    s = Solution()
    print(s.solveNQueens(4))


if __name__ == "__main__":
    main()
