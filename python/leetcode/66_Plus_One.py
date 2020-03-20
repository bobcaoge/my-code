# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        index = -1
        jinwei = 0
        while index >= -len(digits):
            if index == -1:
                buffer = digits[index] + 1 + jinwei
            else:
                buffer = digits[index] + jinwei
            digits[index] = buffer % 10
            jinwei = int(buffer/10)
            index -= 1
            # print(digits, jinwei, buffer)
        if jinwei > 0:
            digits.insert(0, jinwei)

        return digits


def main():
    s = Solution()
    print(s.plusOne([1,2,3]))
    print(s.plusOne([9,9,9]))


if __name__ == "__main__":
    main()
