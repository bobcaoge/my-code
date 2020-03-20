# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def numMovesStonesII(self, stones):
        """
        :type stones: List[int]
        :rtype: List[int]
        """
        stones.sort()
        high = max(stones[-1]-stones[1]+2-len(stones), stones[-2]-stones[0]-len(stones)+2)

        low = len(stones)

        i = 0
        cur = 0
        for j, pos in enumerate(stones):
            cur += 1
            while pos - stones[i] + 1 > len(stones):
                cur -= 1
                i += 1
            if j-i+1 == len(stones)-1 and stones[j]-stones[i] == len(stones)-2:
                low = min(low, 2)
            else:
                low = min(low, len(stones)-cur)
        return [low, high]




def main():
    s = Solution()
    print(s.numMovesStonesII([1,2,5]))
    print(s.numMovesStonesII([1,2,3]))
    print(s.numMovesStonesII([6,5,4,3,10]))
    print(s.numMovesStonesII([4,7,9]))


if __name__ == "__main__":
    main()
