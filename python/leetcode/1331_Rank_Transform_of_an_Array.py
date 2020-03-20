# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        if not arr:
            return []
        ret = [0]*len(arr)
        buff = sorted([(x, i) for i, x in enumerate(arr)])
        last = -1<<31
        rank = 0
        for num, index in buff:
            if num > last:
                last = num
                rank += 1
            ret[index] = rank
        return ret


def main():
    s = Solution()
    print(s.arrayRankTransform([1,1,1]))
    print(s.arrayRankTransform([4,2,30,1,1]))


if __name__ == "__main__":
    main()
