# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        cur = 0
        while start != destination:
            cur += distance[start]
            start = (start+1)%len(distance)
        return min(sum(distance) - cur, cur)


def main():
    s = Solution()
    print(s.distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 1))
    print(s.distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 2))
    print(s.distanceBetweenBusStops([3,6,7,2,9,10,7,16,11]
    ,6
    ,2))


if __name__ == "__main__":
    main()
