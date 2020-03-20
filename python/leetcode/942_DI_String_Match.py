# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        length = len(S)
        max_num = length
        min_num = 0
        ret = [0]*length
        for index, c in enumerate(S):
            if c == "I":
                ret[index] = min_num
                min_num += 1
            else:
                ret[index] = max_num
                max_num -= 1
        ret[-1] = max_num
        return ret
    def diStringMatch1(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        length = len(S)
        max_num = length
        min_num = 0
        ret = []
        for c in S:
            if c == "I":
                ret.append(min_num)
                min_num += 1
            else:
                ret.append(max_num)
                max_num -= 1
        ret.append(max_num)
        return ret


def main():
    s = Solution()


if __name__ == "__main__":
    main()
