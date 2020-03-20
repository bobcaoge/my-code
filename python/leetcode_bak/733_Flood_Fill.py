# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    row = 0
    column = 0
    new_color = 0
    current_color = 0
    image = None

    def change(self, x, y):
        if 0 <= x < self.row and 0 <= y < self.column and self.image[x][y] == self.current_color:
            self.image[x][y] = self.new_color
            self.change(x, y + 1)
            self.change(x, y - 1)
            self.change(x - 1, y)
            self.change(x + 1, y)

    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if not image or newColor == image[sr][sc]:
            return image
        self.row = len(image)
        self.column = len(image[0])
        self.current_color = image[sr][sc]
        self.image = image
        self.new_color = newColor
        self.change(sr, sc)
        return image


def main():
    s = Solution()


if __name__ == "__main__":
    main()
