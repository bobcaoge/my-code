# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def move(self, cells):
        res = [0]*8
        for i in range(1, 7):
            res[i] = 1 if cells[i-1] == cells[i+1] else 0
        return res
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        m = {}
        buff = [0]*266
        for i in range(300):
            # print(cells)
            # print(cells)
            if N == i:
                return cells
            if m.get(tuple(cells), -1) == -1:
                buff[i] = cells
                m[tuple(cells)] = i
                cells = self.move(cells)
            else:
                circle = i - m[tuple(cells)]
                if circle == 1:
                    return cells
                ret = buff[(N-1 - i) % circle + m[tuple(cells)]+1]
                return ret if ret != 0 else cells



def main():
    s = Solution()
    # print(s.prisonAfterNDays(cells = [0,1,0,1,1,0,0,1], N = 1000))
    # print(s.prisonAfterNDays([1,1,0,1,1,0,1,1],
    # 6))
    print(s.prisonAfterNDays([1,0,0,0,1,0,0,1],
    99))


if __name__ == "__main__":
    main()
