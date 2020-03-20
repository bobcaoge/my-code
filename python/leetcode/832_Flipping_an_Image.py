# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = [row[-1::-1] for row in A]
        for i in range(len(A)):
            for j in range(len(A[0])):
                ret[i][j] = 1 - ret[i][j]
        return ret

def main():
    s = Solution()


if __name__ == "__main__":
    main()
