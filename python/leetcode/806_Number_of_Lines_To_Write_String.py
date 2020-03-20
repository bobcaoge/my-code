# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        width_of_having_writed = 0
        lines = 1
        for s in S:
            index = ord(s)-97
            if 100 - width_of_having_writed >= widths[index]:
                width_of_having_writed += widths[index]
            else:
                lines += 1
                width_of_having_writed = widths[index]

        return [lines, width_of_having_writed]


def main():
    s = Solution()


if __name__ == "__main__":
    main()
