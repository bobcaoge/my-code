# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        s = {0}
        for num in stones:
            buff = set()
            while s:
                cur_num = s.pop()
                buff.add(cur_num+num)
                buff.add(cur_num-num)
            s = buff
        return min(abs(x) for x in s)



def main():
    s = Solution()
    print(s.lastStoneWeightII([2,7,4]))
    print(s.lastStoneWeightII([6,6,3,6,3,2,5,1]))
    print(s.lastStoneWeightII([31,26,33,21,40]))


if __name__ == "__main__":
    main()
