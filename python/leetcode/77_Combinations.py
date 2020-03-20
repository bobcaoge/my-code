# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import time


class Solution(object):
    ret = []

    def buffer1(self, s, k, ans):
        if len(ans) + len(s) < k:
            return
        if k == 0:
            self.ret.append(ans)
        else:
            for index, num in enumerate(s):
                self.buffer1(s[index+1:], k-1, ans+[num])

    def combine1(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.ret = []
        if n < k:
            return []
        s = [x+1 for x in range(n)]
        self.buffer1(s, k, [])
        return self.ret

    def buffer2(self, s, k, ans, length_of_ans, length_of_s):
        if length_of_ans + length_of_s < k:
            return
        if k == 0:
            self.ret.append(ans)
        else:
            for index, num in enumerate(s):
                self.buffer2(s[index+1:], k-1, ans+[num], length_of_ans+1, length_of_s-index-1)

    def combine2(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.ret = []
        if n < k:
            return []
        s = [x+1 for x in range(n)]
        self.buffer2(s, k, [], n, 0)
        return self.ret

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n < k:
            return []
        ret = [[[], [x+1 for x in range(n)]]]
        bak = k
        while k != 0:
            buffer = []
            for comb, last in ret:
                for index, num in enumerate(last):
                    if n-index + len(comb) >= bak:
                        buffer.append([comb+[num], last[index+1:]])
            k -= 1
            ret = buffer
            # print(ret)
        return [x[0] for x in ret]

def main():
    s = Solution()
    # print(s.combine(4, 3))

    start = time.time()
    print(s.combine(20, 16))
    end = time.time()
    print(end-start)
    start = end
    print(s.combine1(20, 16))
    end = time.time()
    print(end-start)



if __name__ == "__main__":
    main()
