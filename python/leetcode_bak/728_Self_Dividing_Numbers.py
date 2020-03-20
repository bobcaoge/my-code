# /usr/bin/python2.7
# -*- coding:utf-8 -*-


class Solution(object):
    def judge(self, num):
        """
        :type num: int
        :rtype: bool
        """
        cur = num
        while cur != 0:
            remainder = cur % 10
            if remainder == 0 or num % remainder != 0:
                return False
            cur = cur / 10
        return True

    def selfDividingNumbers1(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        return [num for num in range(left, right+1) if self.judge(num)]
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def judge(num):
            """
            :type num: int
            :rtype: bool
            """
            cur = num
            while cur != 0:
                remainder = cur % 10
                if remainder == 0 or num % remainder != 0:
                    return False
                cur = cur / 10
            return True
        return [num for num in range(left, right+1) if judge(num)]

def main():
    s = Solution()


if __name__ == "__main__":
    main()
