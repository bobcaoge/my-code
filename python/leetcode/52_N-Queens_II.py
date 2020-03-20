# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.queens = [0]*n
        def is_valid(j, num):
            for i in range(j):
                if abs(num-self.queens[i]) == abs(j-i) or num == self.queens[i]:
                    return False
            return True


        def manager(i):
            if i == n:
                return 1
            ret = 0
            for j in range(n):
                if is_valid(i, j):
                    self.queens[i] = j
                    ret += manager(i+1)
            return ret
        return manager(0)



def main():
    s = Solution()


if __name__ == "__main__":
    main()
