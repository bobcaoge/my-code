# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
            return 0
        ret = duration
        for i in range(1, len(timeSeries)):
            diff = timeSeries[i] - timeSeries[i-1]
            if diff <= duration:
                ret += diff
            else:
                ret += duration
        return ret


def main():
    s = Solution()
    print(s.findPoisonedDuration([1,4], 2))
    print(s.findPoisonedDuration([1,2], 2))


if __name__ == "__main__":
    main()
