# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        ret = []
        i = 1
        j = 1+k
        flag = True
        for _ in range(k+1):
            if flag:
                ret.append(i)
                i += 1
            else:
                ret.append(j)
                j -= 1
            flag = not flag
        ret.extend([x for x in range(k+2, n+1)])
        return ret


def main():
    s = Solution()
    print(s.constructArray(10, 5))
    print(s.constructArray(10, 1))


if __name__ == "__main__":
    main()
