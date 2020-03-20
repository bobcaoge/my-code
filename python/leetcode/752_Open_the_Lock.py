# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import heapq


class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        heap = []
        heapq.heappush(heap, (0, "0000"))
        visited = set(deadends)

        m_plus = {}
        m_minus = {}
        for i in range(10):
            m_minus[str(i)] = str((i-1+10)%10)
            m_plus[str(i)] = str((i+1)%10)

        while heap:
            step, cur = heapq.heappop(heap)
            if cur in visited:
                continue
            visited.add(cur)
            if cur == target:
                return step
            # 个位变化
            for i in range(4):
                buff = cur[:i] + m_minus[cur[i]] + cur[i+1:]
                if buff not in visited:
                    heapq.heappush(heap, [step+1, buff])
                buff = cur[:i] + m_plus[cur[i]] + cur[i+1:]
                if buff not in visited:
                    heapq.heappush(heap, [step+1, buff])
        return -1


def main():
    s = Solution()
    print(s.openLock(deadends = ["0201","0101","0102","1212","2002"], target = "0202"))
    print(s.openLock( deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"))


if __name__ == "__main__":
    main()
