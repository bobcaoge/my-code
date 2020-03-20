# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def minHeightShelves(self, books, shelf_width):
        """
        :type books: List[List[int]]
        :type shelf_width: int
        :rtype: int
        """
        dp = [0]*len(books)
        dp[0] = books[0][1]
        for i in range(1, len(books)):
            width, height = books[i]
            dp[i] = dp[i-1] + height
            for j in range(i-1, -1, -1):
                width += books[j][0]
                height = max(height, books[j][1])
                if width > shelf_width:
                    break
                dp[i] = min(dp[i], (dp[j-1] if j-1 >= 0 else 0) + height)
        return dp[-1]


def main():
    s = Solution()
    print(s.minHeightShelves(books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelf_width = 4))
    print(s.minHeightShelves([[7,3],[8,7],[2,7],[2,5]],10))


if __name__ == "__main__":
    main()
