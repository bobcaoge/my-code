# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        j = 0
        for i, num in enumerate(pushed):
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            stack.append(num)
        return stack[::-1] == popped[j:]


def main():
    s = Solution()
    print(s.validateStackSequences(pushed = [1,2,3,4,5], popped = [4,5,3,2,1]))


if __name__ == "__main__":
    main()
