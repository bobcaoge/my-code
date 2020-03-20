# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = []
        ret = 0
        for i, height in enumerate(heights):
            pos = i
            while stack and stack[-1][0] > height:
                ret = max(ret, stack[-1][0]*(i-stack[-1][-1]))
                pos = stack.pop()[1]
            stack.append([height, pos])
        return ret


def main():
    s = Solution()
    print(s.largestRectangleArea([2,1,5,6,2,3]))
    print(s.largestRectangleArea([2,3,4,5,6,1,6,5,4,3,2]))
    print(s.largestRectangleArea([4,2,0,3,2,5]))
    print(s.largestRectangleArea([1,3,3]))
    print(s.largestRectangleArea([2,0]))


if __name__ == "__main__":
    main()
