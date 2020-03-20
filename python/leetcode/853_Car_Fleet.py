# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        fleets = len(position)
        info_of_car = list(zip(position, speed))
        info_of_car.sort()

        old_position = target
        old_speed = 1000000
        for i in range(len(info_of_car)-1, -1, -1):

            if (target-info_of_car[i][0]) / info_of_car[i][1] <= (target-old_position) / old_speed:
                fleets -= 1
            else:
                old_position = info_of_car[i][0]
                old_speed = info_of_car[i][1]

        return fleets



def main():
    s = Solution()
    print(s.carFleet(12, position = [10,8,0,5,3], speed = [2,4,1,1,3]))
    print(s.carFleet(10,[0,2,4],[2,3,1]))


if __name__ == "__main__":
    main()
