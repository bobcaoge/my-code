# /usr/bin/python3.6
# -*- coding:utf-8 -*-
from heapq import *

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums2 or not nums1:
            return []
        heap = []
        ret = []
        heappush(heap, [nums1[0]+nums2[0], 0, 0])
        while len(ret) < k and heap:
            min_of_cur = heappop(heap)
            _, i, j = min_of_cur
            ret.append([nums1[i], nums2[j]])
            if j+1 < len(nums2):
                heappush(heap, [nums1[i]+nums2[j+1], i, j+1])
            if j == 0 and i+1 < len(nums1):
                heappush(heap, [nums1[i+1]+nums2[j], i+1, j])
        return ret

    def kSmallestPairs3(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums2 or not nums1:
            return []
        heap = []
        visited = set()
        ret = []
        heappush(heap, [nums1[0]+nums2[0], 0, 0])
        visited.add((0, 0))
        while len(ret) < k and heap:
            min_of_cur = heappop(heap)
            _, i, j = min_of_cur
            ret.append([nums1[i], nums2[j]])

            if i+1 < len(nums1) and (i+1, j) not in visited:
                heappush(heap, [nums1[i+1]+nums2[j], i+1, j])
                visited.add((i+1, j))

            if j+1 < len(nums2) and (i, j+1) not in visited:
                heappush(heap, [nums1[i]+nums2[j+1], i, j+1])
                visited.add((i, j+1))
        return ret


    def kSmallestPairs1(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums2 or not nums1:
            return []
        ret = []
        for x in nums1[:k]:
            for y in nums2[:k]:
                ret.append([x+y, [x, y]])
        return [x[1] for x in sorted(ret)[:k]]

    def kSmallestPairs2(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums2 or not nums1:
            return []
        nums1 = nums1[:k]
        nums2 = nums2[:k]
        length1 = len(nums1)
        length2 = len(nums2)
        record = [0]*k if length1 >= k else [0]*length1
        ret = [[nums1[0], nums2[0]]]
        record[0] += 1
        for index in range(1, k):
            last = 2**32
            cur = None
            index_of_record = -1
            for i, j in enumerate(record):
                if j < length2:
                    if nums1[i]+nums2[j] < last:
                        cur = [nums1[i], nums2[j]]
                        last = nums1[i]+nums2[j]
                        index_of_record = i
            if cur is not None:
                ret.append(cur)
                if record[index_of_record] < length2:
                    record[index_of_record] += 1
            else:
                break
        return ret


def main():
    s = Solution()
    print(s.kSmallestPairs([1,1,3], [1,1,4], 10))
    print(s.kSmallestPairs([1,1,2], [1,2,3], 10))


if __name__ == "__main__":
    main()
