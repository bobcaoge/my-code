# /usr/bin/python3.6
# -*- coding:utf-8 -*-

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        start = 0
        last_left = 0
        end = length-1
        last_end = 0
        max_water = 0
        while start < end:
            # print(last_left, last_end)
            if height[start] >= last_left and height[end] >= last_end:
                max_water = max((end-start)*min(height[start], height[end]), max_water)
                last_left, last_end = height[start], height[end]
                if last_left < last_end:
                    start += 1
                else:
                    end -= 1
            elif height[start] >= last_left:
                end -= 1
            elif height[end] >= last_end:
                start += 1
            else:
                end -= 1
                start += 1
        return max_water


def main():
    s = Solution()
    a = [1,8,6,2,5,4,8,3,7]
    print(s.maxArea(a))
    a = [1, 2]
    print(s.maxArea(a))


if __name__ == "__main__":
    main()
