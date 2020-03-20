# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        left = 0
        right = len(people)-1
        ret = 0
        people.sort()
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            ret += 1
        return ret



def main():
    s = Solution()
    print(s.numRescueBoats([3,2,2,1], limit = 3))


if __name__ == "__main__":
    main()
