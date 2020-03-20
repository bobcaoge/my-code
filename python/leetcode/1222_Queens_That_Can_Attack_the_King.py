# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        cur = []
        x, y = king
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                cur.append([x, y, dx, dy])
        ret = []
        while cur:
            buff = []
            for x, y, dx, dy in cur:
                if 0<= x+dx < 8 and 0 <= y+dy < 8:
                    if [x+dx, y+dy] in queens:
                        ret.append([x+dx, y+dy])
                    else:
                        buff.append([x+dx, y+dy, dx, dy])
            cur = buff
        return ret


def main():
    s = Solution()
    print(s.queensAttacktheKing([[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]))
    print(s.queensAttacktheKing(queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]))
    print(s.queensAttacktheKing(queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]], king = [3,4]))

if __name__ == "__main__":
    main()
