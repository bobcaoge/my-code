# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return 0
        dp1 = [0]*len(ratings)
        dp2 = [0]*len(ratings)
        dp1[0] = dp2[-1] = 1
        length = len(ratings)
        for i in range(1, len(ratings)):
            dp1[i] = dp1[i-1]+1 if ratings[i] > ratings[i-1] else 1
            dp2[length-1-i] = dp2[length-i]+1 if ratings[length-1-i] > ratings[length-1-i+1] else 1
        return sum([max(dp2[i], dp1[i]) for i in range(len(ratings))])


def main():
    s = Solution()
    print(s.candy([1,0,2]))
    print(s.candy([1,3,3]))
    print(s.candy([1,0,2,4,2,7,3,4,2,4,6,8,5,4,2,5,6,4,5,4,45,5]))


if __name__ == "__main__":
    main()
