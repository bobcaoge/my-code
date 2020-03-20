# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def calc_the_length_of_edge(self, point1, point2):
        return ((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)**0.5

    def calc_the_area_of_triangle(self, point1, point2, point3):
        edge1 = self.calc_the_length_of_edge(point1, point2)
        edge2 = self.calc_the_length_of_edge(point1, point3)
        edge3 = self.calc_the_length_of_edge(point2, point3)
        if edge1 + edge2 <= edge3:
            return 0
        if edge1 + edge3 <= edge2:
            return 0
        if edge3 + edge2 <= edge1:
            return 0
        avg = (edge1+edge2+edge3)/2.0
        return (avg*(avg-edge1)*(avg-edge2)*(avg-edge3))**0.5

    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        ret = 0
        length = len(points)
        for i in range(length):
            for j in range(i+1, length):
                for k in range(j+1, length):
                    ret = max(ret, self.calc_the_area_of_triangle(points[i], points[j], points[k]))
        return ret



def main():
    s = Solution()
    print(s.largestTriangleArea([[35,-23],[-12,-48],[-34,-40],[21,-25],[-35,-44],[24,1],[16,-9],[41,4],[-36,-49],[42,-49],[-37,-20],[-35,11],[-2,-36],[18,21],[18,8],[-24,14],[-23,-11],[-8,44],[-19,-3],[0,-10],[-21,-4],[23,18],[20,11],[-42,24],[6,-19]]))


if __name__ == "__main__":
    main()
