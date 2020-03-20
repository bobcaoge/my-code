# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        if len(timePoints) > 1440:
            return 0
        timePoints.sort()
        ret = 60*24
        for i in range(len(timePoints)-1):
            diff = self.get_time_diff(timePoints[i], timePoints[i+1])
            ret = min(ret, diff, 1440-diff)
        diff = self.get_time_diff(timePoints[0], timePoints[-1])
        ret = min(ret, diff, 1440-diff)
        return ret

    def get_time_diff(self, p1, p2):
        s1 = p1.split(":")
        s2 = p2.split(":")
        return (int(s2[0])-int(s1[0]))*60+(int(s2[1])-int(s1[1]))


def main():
    s = Solution()
    print(s.findMinDifference(["00:00", "23:59", ""]))



if __name__ == "__main__":
    main()
