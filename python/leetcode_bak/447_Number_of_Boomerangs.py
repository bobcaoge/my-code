# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):

    def get_distance(self,point1, point2):
        return (point1[0]-point2[0])**2 + (point1[1]-point2[1])**2

    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ret = 0
        for point1 in points:
            p_map = {}
            for point2 in points:
                distance = self.get_distance(point1, point2)
                p_map[distance] = 1 + p_map.get(distance, 0)

            for k in p_map.values():
                ret += k*(k-1)
        return ret





def main():
    s = Solution()


if __name__ == "__main__":
    main()
