# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def containsNearbyDuplicate1(self, nums, k):
        """
        超时
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        table = {}
        for index in range(len(nums)):
            if table.keys().__contains__(nums[index]):
                old_places = table[nums[index]]
                if index - old_places <= k:
                    return True
                table[nums[index]] = index
            else:
                table[nums[index]] = index
        print(table)
        return False

    def containsNearbyDuplicate(self, nums, k):
        """

        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        s = set()
        for index, num in enumerate(nums):

            if index > k:
                s.remove(nums[index-k-1])
            if s.__contains__(num):
                return True
            s.add(num)
        return False



def main():
    s = Solution()
    print(s.containsNearbyDuplicate([1,2,3,1,2,3],2))
    print(s.containsNearbyDuplicate([1,0,1,1],2))

if __name__ == "__main__":
    main()
