# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        self.ret = []
        def dfs(num):
            if low<= num <= high:
                self.ret.append(num)
            if num > high:
                return

            a = num % 10
            if a < 9:
                dfs(num*10+a+1)
        for i in range(1, 10):
            dfs(i)
        return sorted(self.ret)


def main():
    s = Solution()
    print(s.sequentialDigits(100, 300))
    print(s.sequentialDigits(1000, 13000))


if __name__ == "__main__":
    main()
