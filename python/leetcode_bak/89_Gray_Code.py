# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        s = set([x for x in range(1, 2**n)])
        ret = [0]
        while True:
            change = False
            base = 0
            for i in range(n):
                buff = ret[-1] ^ 2**base
                if buff in s:
                    ret.append(buff)
                    s.remove(buff)
                    change = True
                    break
                base += 1
            if not change:
                break
        return ret



def main():
    s = Solution()
    print(s.grayCode(0))


if __name__ == "__main__":
    main()
