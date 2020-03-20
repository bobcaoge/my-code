# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        """
        :type restaurants: List[List[int]]
        :type veganFriendly: int
        :type maxPrice: int
        :type maxDistance: int
        :rtype: List[int]
        """
        cur = []
        for id, r, v, p, d in restaurants:
            if v >= veganFriendly and p <= maxPrice and d <= maxDistance:
                cur.append([r, id])
        return [id for _, id in sorted(cur, reverse=True)]


def main():
    s = Solution()


if __name__ == "__main__":
    main()
