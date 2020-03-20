# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        ret = [0]*len(T)
        stack.append(0)
        for i in range(1, len(T)):
            while stack and T[stack[-1]] < T[i]:
                ret[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return ret



def main():
    s = Solution()


if __name__ == "__main__":
    main()
