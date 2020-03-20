# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        mask1 = 1<<7
        mask2 = 1<<6
        n_byte = 0
        for num in data:
            mask = 1<<7
            if n_byte == 0:
                while mask & num:
                    n_byte += 1
                    mask >>= 1
                if n_byte == 0:
                    continue
                if n_byte > 4 or n_byte == 1:
                    return False
                n_byte -= 1
            else:
                if not (num & mask1) or (num & mask2):
                    return False
                n_byte -= 1

        return n_byte == 0

    def validUtf8_1(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        n_byte = 0
        for num in data:
            bin_s = format(num, "#010b")[-8:]

            if n_byte == 0:
                for c in bin_s:
                    if c == "0":
                        break
                    n_byte += 1
                if n_byte == 0:
                    continue

                if n_byte > 4 or n_byte == 1:
                    return False
                n_byte -= 1
            else:
                if bin_s[0] != "1" or bin_s[1] != "0":
                    return False
                n_byte -= 1
        return n_byte == 0


def main():
    s = Solution()
    # print(s.validUtf8([197,130,1]))
    print(s.validUtf8([240,162,138,147]))


if __name__ == "__main__":
    main()
