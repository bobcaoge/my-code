# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        record = []
        for i in range(32):
            record.append(self.get_info(1<<i))
        target = self.get_info(N)
        return target in record

    def get_info(self, num):
        ret = [0]*10
        for c in str(num):
            ret[ord(c)-ord('0')] += 1
        return ret


def main():
    s = Solution()
    print(s.reorderedPowerOf2(16))


if __name__ == "__main__":
    main()
