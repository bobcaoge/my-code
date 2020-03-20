# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k <= 0 or t < 0:
            return False
        m = {}
        for i, num in enumerate(nums):
            m[num] = m.get(num, [])+[i]

        s = set()
        for num, indexes in m.items():
            for i in range(len(indexes)):
                for j in range(i+1, len(indexes)):
                    if indexes[j] - indexes[i] <= k:
                        return True
            s.add((num, num))
        if t > 0:
            for num, indexes in m.items():
                for another_num, indexes_of_another_num in m.items():
                    key = tuple(sorted([num, another_num]))
                    if key not in s and abs(another_num - num) <= t:
                            i = 0
                            while i < len(indexes):
                                j = 0
                                while j < len(indexes_of_another_num):
                                    if abs(indexes[i]-indexes_of_another_num[j]) <= k:
                                        return True
                                    j += 1
                                i += 1
                    s.add(key)

        return False



def main():
    s = Solution()
    print(s.containsNearbyAlmostDuplicate([1, 2], 0, 1))
    print(s.containsNearbyAlmostDuplicate([1,2,3,1],3,0))
    print(s.containsNearbyAlmostDuplicate([1,0,1,1],1,2))
    print(s.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3))
    print(s.containsNearbyAlmostDuplicate([1,3,1], 2, 1))
    print(s.containsNearbyAlmostDuplicate([-1,-1], 1, -1))

if __name__ == "__main__":
    main()
