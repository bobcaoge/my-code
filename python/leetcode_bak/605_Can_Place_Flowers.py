# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed = [1, 0] + flowerbed + [0, 1]
        cur = 0
        result = 0
        for flower in flowerbed:
            if flower == 0:
                cur += 1
            else:
                result += int((cur-1)/2)
                cur = 0
        return result >= n


    def canPlaceFlowers1(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        s = ("10"+"".join([str(x) for x in flowerbed])+"01").split("1")
        print(s)
        result = 0
        for x in s:
            result += int((len(x) - 1) / 2) if len(x) > 0 else 0
        print(result)
        return result >= n

def main():
    s = Solution()
    print(s.canPlaceFlowers([1,0,0,0,1],1))
    print(s.canPlaceFlowers([0,0],1))


if __name__ == "__main__":
    main()
