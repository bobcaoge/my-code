# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        w = max(sum(weights) / D, max(weights))
        start = w
        end = sum(weights)
        mid = (start+end)/2
        days_of_mid = self.get_days_needed(weights, mid)
        # print(self.get_days_needed(weights, 7))
        # print(self.get_days_needed(weights, 11))
        while start < end:
            if days_of_mid <= D:
                if self.get_days_needed(weights, mid-1) > D:
                    return mid
                end = mid - 1
            else:
                start = mid + 1
            mid = (start+end)/2
            days_of_mid = self.get_days_needed(weights, mid)
        return start

    def get_days_needed(self,weights, weight):
        days = 0
        weight_keep = weight
        for w in weights:
            weight -= w
            if weight < 0:
                days += 1
                weight = weight_keep - w
        if weight >= 0:
            days += 1
        return days





def main():
    s = Solution()
    print(s.shipWithinDays([1,2,3,4,5,6,7,8,9,10], D = 5))
    print(s.shipWithinDays([3,2,2,4,1,4], D = 3))
    print(s.shipWithinDays(weights = [1,2,3,1,1], D = 4))


if __name__ == "__main__":
    main()
