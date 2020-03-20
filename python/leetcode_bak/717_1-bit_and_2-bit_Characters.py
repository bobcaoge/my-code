# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        index = 0
        length = len(bits)
        one_flag = False
        while index < length:
            if bits[index] == 0:
                one_flag = True
                index += 1
            else:
                one_flag = False
                index += 2
        return one_flag



def main():
    s = Solution()


if __name__ == "__main__":
    main()
