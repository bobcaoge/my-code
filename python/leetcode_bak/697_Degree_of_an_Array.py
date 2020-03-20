# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = {}
        for index, num in enumerate(nums):
            if m.get(num, None):
                m[num][1].append(index)
                m[num][0] += 1
            else:
                m[num] = [1, [index]]
        frequency_record = -1
        length_record = -1
        for num, info in m.items():
            length = info[1][-1]-info[1][0]+1
            frequency = info[0]
            if frequency > frequency_record:
                frequency_record = frequency
                length_record = length
            elif frequency_record == frequency:
                if length < length_record:
                    length_record = length
        return length_record

    def findShortestSubArray1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = {}
        for index, num in enumerate(nums):
            if m.get(num, None):
                m[num][1].append(index)
                m[num][0] += 1
            else:
                m[num] = [1, [index]]
        frequency_record = -1
        length_record = -1
        for num, info in m.items():
            indexes = info[1]
            length = indexes[-1]-indexes[0]+1 if indexes[-1] > indexes[0] else 1
            frequency = info[0]
            if frequency_record == 0:
                length_record = length
                frequency_record = frequency
            else:
                if frequency > frequency_record:
                    frequency_record = frequency
                    length_record = length
                elif frequency_record == frequency:
                    if length < length_record:
                        length_record = length
        return length_record


def main():
    s = Solution()


if __name__ == "__main__":
    main()
