# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        cur_distance = 0
        max_distance = 0
        flag = True
        for i, seat in enumerate(seats):
            if seat == 1:
                if flag:
                    max_distance = cur_distance
                    flag = False
                else:
                    if (cur_distance+1)/2 > max_distance:
                        max_distance = (cur_distance+ 1)/2
                cur_distance = 0
            else:
                cur_distance += 1
        return max(max_distance, cur_distance)





def main():
    s = Solution()


if __name__ == "__main__":
    main()
