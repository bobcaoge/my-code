# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        rate = []
        for i in range(1, len(coordinates)):
            cur_rate = (coordinates[i][1] - coordinates[0][1])/(coordinates[i][0] - coordinates[0][0] if (coordinates[i][0] - coordinates[0][0]) != 0 else 1.5)
            if not rate:
                rate.append(cur_rate)
            else:
                if rate[-1] != cur_rate:
                    return False
        return True




def main():
    s = Solution()
    print(s.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))


if __name__ == "__main__":
    main()
