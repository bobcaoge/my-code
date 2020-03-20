# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i in range(1, len(triangle)):
            length = triangle[i]
            for j in range(length):
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                elif j == length - 1:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
        return min(triangle[-1])





def main():
    s = Solution()


if __name__ == "__main__":
    main()
