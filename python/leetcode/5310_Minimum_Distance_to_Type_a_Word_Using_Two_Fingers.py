# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import heapq


class Solution(object):
    def minimumDistance(self, word):
        """
        :type word: str
        :rtype: int
        """
        latter = [['A', 'B', 'C', 'D', 'E', 'F'],
                  ['G', 'H', 'I', 'J', 'K', 'L'],
                  ['M', 'N', 'O', 'P', 'Q', 'R'],
                  ['S', 'T', 'U', 'V', 'W', 'X'],
                  ['Y', 'Z', '', '','', '',]]
        coor = {}
        for i in range(len(latter)):
            for j in range(len(latter[0])):
                coor[latter[i][j]] = (i, j)
        def get_distance(a, b):
            x1, y1 = coor[a]
            x2, y2 = coor[b]
            return abs(x1-x2)+abs(y1-y2)

        heap = []
        heapq.heappush(heap, [0, [0, -1]])
        s = set()
        while heap:
            step, [first_finger, second_finger] = heapq.heappop(heap)
            next_pos = max(first_finger, second_finger)+1
            if (first_finger, second_finger) in s:
                continue
            s.add((first_finger, second_finger))
            if next_pos >= len(word):
                return step
            if first_finger == -1:
                heapq.heappush(heap, [step,[next_pos, second_finger]])
            else:
                heapq.heappush(heap, [step+get_distance(word[first_finger], word[next_pos]),[next_pos, second_finger]])
            if second_finger == -1:
                heapq.heappush(heap, [step,[first_finger, next_pos]])
            else:
                heapq.heappush(heap, [step+get_distance(word[second_finger], word[next_pos]),[first_finger, next_pos]])


def main():
    s = Solution()
    print(s.minimumDistance("CAKE"))
    print(s.minimumDistance("OPVUWZLCKTDPSUKGHAXIDWHLZFKNBDZEWHBSURTVCADUGTSDMCLDBTAGFWDPGXZBVARNTDICHCUJLNFBQOBTDWMGILXPSFWVGYBZVFFKQIDTOVFAPVNSQJULMVIERWAOXCKXBRI"))


if __name__ == "__main__":
    main()
